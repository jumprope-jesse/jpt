---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/integrate-amazon-aurora-mysql-and-amazon-bedrock-using-sql/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-11T18:50:00.000Z
---

# Integrate Amazon Aurora MySQL and Amazon Bedrock using SQL | Amazon Web Services

## AI Summary (from Notion)
- Integration of Technologies: The document discusses the integration of Amazon Aurora MySQL with Amazon Bedrock to enhance relational databases using generative AI models.

- Use Cases:
- Service Improvement: Utilizes Amazon Bedrock to supplement existing database information for real-time access.
- Productivity Enhancement: Summarizes long texts stored in Aurora databases using generative AI.

- Key Components:
- Amazon Aurora: A cloud-based RDBMS compatible with MySQL and PostgreSQL, optimized for performance and cost-effectiveness.
- Amazon Bedrock: A fully managed service providing access to foundation models (FMs) for building generative AI applications.

- Solution Overview:
- Explains the role of generative AI and foundation models in creating new content and enhancing user experiences.
- Highlights the ease of using SQL commands for machine learning tasks without requiring prior ML experience.

- Implementation Steps:
- Creating an Aurora MySQL cluster and configuring it for Bedrock integration.
- Setting up IAM roles and policies to allow Aurora access to Amazon Bedrock.
- Running SQL queries to leverage generative AI functions for database operations.

- Demonstration of Functionality:
- Examples provided for creating functions to invoke FMs from Amazon Bedrock.
- Procedures for using SQL to retrieve and summarize data using AI models.

- Considerations:
- Emphasizes the importance of adapting implementations for production use and understanding cost implications of using Bedrock.

- Conclusion:
- Highlights the potential of augmenting relational databases with generative AI to improve user experiences and productivity.
- Encourages readers to explore Aurora ML and its integration capabilities for generative AI applications.

- Interesting Fact:
- The document mentions that LLMs can perform a variety of language-based tasks, emphasizing the versatility of foundation models in enhancing data management and user interaction.

## Content (from Notion)

Because organizations store a large amount of their data in relational databases, there is a clear impetus to augment these datasets using generative artificial intelligence (AI) foundation models to elevate end-user experiences. In this post, we explore how to integrate Amazon Aurora MySQL-Compatible Edition with a generative AI model using Amazon Aurora Machine Learning. We walk through the Amazon Aurora MySQL integration with Amazon Bedrock and demonstrate two use cases:

- Complementing database information for service improvement – Obtain supplemental information using Amazon Bedrock and store it in an Aurora database for real-time access
- Improving productivity – Summarize a long text stored in an Aurora database using Amazon Bedrock
To learn about other ways to use ML with Amazon Aurora MySQL, refer to Build a generative AI- powered agent assistance application using Amazon Aurora and Amazon SageMaker JumpStart.

## Solution overview

Generative AI is a type of AI that can create new content and ideas, including conversations, stories, images, videos, and music.

Foundation models (FMs) are machine learning (ML) models trained on a broad spectrum of generalized and unlabeled data. They’re capable of performing a wide variety of general tasks. Large language models (LLMs) are a class of FMs. LLMs are specifically focused on language-based tasks such as such as summarization, text generation, classification, open-ended conversation, and information extraction.

The solution is based on the following key components:

- Amazon Aurora – Amazon Aurora is a relational database management system (RDBMS) built for the cloud with MySQL and PostgreSQL compatibility. Aurora gives you the performance and availability of commercial-grade databases at one-tenth the cost. Aurora ML enables you to call a wide variety of ML algorithms, including ML-based predictions, generative AI, and sentiment analysis, using the familiar SQL programming language. You don’t need prior ML experience to use Aurora ML. Aurora ML provides straightforward, optimized, and secure integration between Aurora and AWS ML services without having to build custom integrations or move data around. Aurora calls Amazon SageMaker for a wide variety of ML algorithms, including FMs, Amazon Comprehend for sentiment analysis, and Amazon Bedrock models, so your application doesn’t need to call these services directly.
- Amazon Bedrock – Amazon Bedrock is a fully managed service that offers a choice of high-performing FMs from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon via a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. Amazon Bedrock offers a straightforward way to build and scale generative AI applications with FMs. Because Amazon Bedrock is serverless, you don’t have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications using the AWS services you are already familiar with.
This following diagram illustrates an example of using ML with Amazon Aurora MySQL.

In the following sections, we demonstrate how to make real-time calls to Amazon Bedrock using SQL queries from Amazon Aurora MySQL. The high-level steps are as follows:

1. Create a new cluster.
1. Create a database and database user.
1. Create an AWS Identity and Access Management (IAM) role and policy for the Aurora cluster.
1. Assign the IAM role to the Aurora cluster.
1. Use Aurora ML by enabling Amazon Bedrock base models.
1. Create functions for accessing Amazon Bedrock.
## Prerequisites

This post assumes familiarity with navigating the AWS Management Console. For this solution, you’ll also need the following resources and services enabled in your AWS account:

- Amazon Aurora MySQL 3.06.0 or later version is required to use Amazon Bedrock integration.
- The Aurora MySQL cluster must use a custom DB cluster parameter group.
- IAM access is required to create roles and permissions. You must have access to use specific FMs in Amazon Bedrock.
- In this post, we use Amazon Titan Text G1 – Express (amazon.titan-text-express-v1) and Anthropic Claude 3 Haiku (anthropic.claude-3-haiku-20240307-v1:0).
- The ML services must be running in the same AWS Region as your Aurora MySQL cluster.
- The network configuration of your Aurora MySQL cluster must allow outbound connections to endpoints for Amazon Bedrock.
## Create an Aurora MySQL cluster

The first step is to create an Aurora MySQL cluster. For full instructions, refer to Creating and connecting to an Aurora MySQL DB cluster and Using Amazon Aurora machine learning with Aurora MySQL. We highlight a few specific configuration options used in this example:

1. On the Aurora console, create a new cluster in a Region that supports Amazon Bedrock. (For example, us-east-1)
1. For Engine options, select Aurora (MySQL Compatible). For Engine version, we use Aurora MySQL 3.06.0 for using Amazon Bedrock integration.
1. For Configuration options, select either Aurora Standard or Aurora I/O Optimized.
1. For DB instance class, select your instance class.
1. For Amazon Bedrock, you need to modify the parameter group later, so you should apply custom DB cluster parameter group at this time.
1. Create your Aurora cluster. After the cluster is provisioned, you need to run a series of SQL commands to prepare your cluster for integrating with Amazon Bedrock.
1. Log in to your Aurora cluster either as a user with the rds_superuser_role privilege, such as the master user by using MySQL Command-Line Client, and run the following code. The AWS_BEDROCK_ACCESS database role must be granted to the user in order to work with Amazon Bedrock ML functions.
```plain text
mysql> create database bedrockdb;  /*** Sample Database ***/
Query OK, 1 row affected (0.03 sec)

mysql> create user `bedrock_user`@`%` identified by 'password'; /*** Sample User ***/
Query OK, 0 rows affected (0.30 sec)

mysql> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, INDEX, CREATE ROUTINE, ALTER ROUTINE, EXECUTE ON bedrockdb.* TO `bedrock_user`@`%`;
Query OK, 0 rows affected (0.05 sec)

mysql> GRANT AWS_BEDROCK_ACCESS TO `bedrock_user`@`%`;
Query OK, 0 rows affected (0.01 sec)

mysql> SHOW GRANTS FOR `bedrock_user`@`%`\G
*************************** 1. row ***************************
Grants for bedrock_user@%: GRANT USAGE ON *.* TO `bedrock_user`@`%`
*************************** 2. row ***************************
Grants for bedrock_user@%: GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, EXECUTE, CREATE ROUTINE, ALTER ROUTINE ON `bedrockdb`.* TO `bedrock_user`@`%`
*************************** 3. row ***************************
Grants for bedrock_user@%: GRANT `AWS_BEDROCK_ACCESS`@`%` TO `bedrock_user`@`%`

```

Your database user is now set up to integrate with Amazon Bedrock. Now you can create an IAM role to provide the Aurora MySQL DB cluster access to Amazon Bedrock.

## Create an IAM role and policy for the Aurora cluster

To allow Aurora ML to work with Amazon Bedrock, you first create an IAM policy that allows the Aurora cluster to communicate with Amazon Bedrock models. Complete the following steps:

1. On the IAM console, choose Policies in the navigation pane.
1. Choose Create policy.
1. On the Specify permissions page, for Select a service, choose Bedrock.
1. For Resources, select All or Specific. As a best practice, make sure to only give access to models in Amazon Bedrock that your team requires.
1. Choose Next.
1. For Policy name, enter a name for your policy, such as AuroraBedrockInvokeModel.
1. Choose Create policy.
1. On the IAM console, choose Roles in the navigation pane.
1. Choose Create role.
1. For Trusted entity type, select AWS service.
1. For Service or use case, choose RDS.
1. Select RDS – Add Role to Database.
1. Choose Next.  Now you assign the IAM policy you created in the previous step to this IAM role.
1. For Permission policies, find and select the AuroraBedrockInvokeModel policy.
1. Choose Next.
1. In the Role details section, enter a name (for this post, AuroraBedrockRole) and a description.
1. Review the IAM role and confirm that the AuroraBedrockInvokeModel policy is attached.
1. Choose Create to create the role.
## Assign the IAM role to the Aurora cluster

Now you need to assign the AuroraBedrockRole IAM role to the Amazon Aurora MySQL cluster. Complete the following steps:

1. On the Amazon RDS console, navigate to your Aurora MySQL cluster details page.
1. On the Connectivity & security tab, locate the Manage IAM roles section.
1. Select IAM roles to add to this cluster, choose the AuroraBedrockRole role.
1. Choose Add role.
1. Add the ARN of this IAM role to the aws_default_bedrock_role parameter of the custom DB cluster parameter group associated with your Aurora MySQL cluster.
1. Choose Save changes to save the setting.
You can confirm the parameters by using the AWS Management Console or AWS Command Line Interface (AWS CLI). You can also check using the MySQL Client tool as shown in the following example:

```plain text
mysql> show global variables like 'aws_default%';
+-----------------------------+--------------------------------------------------+
| Variable_name               | Value                                            |
+-----------------------------+--------------------------------------------------+
| aws_default_bedrock_role    | arn:aws:iam::012345678910:role/AuroraBedrockRole |
| aws_default_comprehend_role |                                                  |
| aws_default_lambda_role     |                                                  |
| aws_default_s3_role         |                                                  |
| aws_default_sagemaker_role  |                                                  |
+-----------------------------+--------------------------------------------------+
5 rows in set (0.03 sec)
```

Your cluster can now invoke models in Amazon Bedrock.

## Use Aurora ML

Aurora ML is an Aurora feature that lets builders work directly with AWS ML services using SQL commands, including Amazon Bedrock, SageMaker, and Amazon Comprehend.

You can list the Amazon Bedrock FMs using the AWS CLI:

```plain text
$ aws bedrock list-foundation-models --query '*[].[modelName,modelId]' --out table
-------------------------------------------------------------------------------
|                            ListFoundationModels                             |
+---------------------------------+-------------------------------------------+
|  Titan Text Large               |  amazon.titan-tg1-large                   |
|  Titan Image Generator G1       |  amazon.titan-image-generator-v1:0        |
|  Titan Image Generator G1       |  amazon.titan-image-generator-v1          |
|  Titan Text Embeddings v2       |  amazon.titan-embed-g1-text-02            |
|  Titan Text G1 - Lite           |  amazon.titan-text-lite-v1:0:4k           |
|  Titan Text G1 - Lite           |  amazon.titan-text-lite-v1                |
...
|  Claude                         |  anthropic.claude-v2:1:200k               |
|  Claude                         |  anthropic.claude-v2:1                    |
|  Claude                         |  anthropic.claude-v2                      |
|  Claude 3 Sonnet                |  anthropic.claude-3-sonnet-20240229-v1:0  |
|  Claude 3 Haiku                 |  anthropic.claude-3-haiku-20240307-v1:0   |
+---------------------------------+-------------------------------------------+

```

Before you use base models, make sure the target model is enabled on the Amazon Bedrock Console. If it’s not enabled, please add model access to the target model.

You are now able to create functions that allow you to directly access Amazon Bedrock from Aurora. The following example shows how to generate a function using Amazon Titan Text G1 – Express and Anthropic Claude 3 Haiku model on Amazon Bedrock which supports the TEXT modality. If you want to use different model ID, refer to Base model IDs for the model ID and Supported foundation models in Amazon Bedrock for a list of supported models.

1. Log in with the bedrock_user account that you created earlier.
1. Navigate to the bedrockdb database and create functions after setting the role to AWS_BEDROCK_ACCESS. The function definitions are provided in the GitHub repository. 
1. Create a function to call Amazon Titan Text G1 -Express: 
1. Create a function to call Anthropic Claude 3 Haiku: 
1. Ask “What is the proportion of land and sea on Earth?” and invoke an Amazon Titan function: 
1. Invoke an Anthropic Claude 3 function: 
You can verify the correctness of the response by checking the output of the question in Amazon Bedrock playgrounds on the Amazon Bedrock console. Refer to Anthropic’s Claude 3 Haiku model is now available on Amazon Bedrock for more information.

Now you have finished preparing your Aurora cluster to use Amazon Bedrock.

In the following sections, we demonstrate two use cases to use existing data integrated with Amazon Bedrock.

If the Aurora cluster you created can’t communicate with Amazon Bedrock, you may need to adjust the network configuration so your Aurora cluster can communicate with Amazon Bedrock. For more information on how to do this, see Enabling network communication from Amazon Aurora MySQL to other AWS services, Create a VPC endpoint and Use AWS PrivateLink to set up private access to Amazon Bedrock. In this post, we choose the bedrock-runtime endpoint for using a private connection between the VPC and Amazon Bedrock.

### Use case 1: Complement existing data with Amazon Bedrock

Let’s see how you can complement the information by linking existing data with Amazon Bedrock. In this example, you don’t have data in this database yet, so you create a table and add data for verification purposes. The table definition is provided in the GitHub repository.

1. Create a sample table: 
1. Insert sample data (assume that this is existing data stored in your database): 
1. Check that the data is stored in the table.
1. Create a procedure for retrieving data from the table then run the function for the data. The procedure definition is provided in the GitHub repository: 
1. Run the procedure which retrieves data from an existing table, requests Amazon Bedrock based on the target data, retrieves the data according to the contents, and updates the contents of the table: 
As a result, you should be able to obtain complementary information for your data.

The following example show your output, which lists popular food from different countries:

```plain text
mysql> select * from t_bedrock limit 1\G
```

For example, if you’re running a travel site and want to post tourist spots in Kyoto as reference information on your site, you can change the inquiry content as shown in the following example to obtain data. The data required varies depending on the use case, so try customizing the inquiry according to your needs:

```plain text
select json_unquote(json_extract(claude3_haiku(
'{
 "anthropic_version": "bedrock-2023-05-31",
 "max_tokens": 1024,"temperature": 0,"top_p": 0,"top_k":1,"stop_sequences": [],
 "messages": [{"role": "user","content": [{"type": "text", "text": "Please tell me 3 recommended sightseeing spots in Kyoto."}]}]
}'),"$.content[0].text")) as response_from_bedrock\G
```

Anthropic Claude 3 supports English, Spanish, Japanese, and multiple other languages. For example, the following request asks for five recommended sightseeing spots in Kyoto in Japanese:

```plain text
select json_unquote(json_extract(claude3_haiku(
'{
 "anthropic_version": "bedrock-2023-05-31",
 "max_tokens": 1024,"temperature": 0,"top_p": 0,"top_k":1,"stop_sequences": [],
 "messages": [{"role": "user","content": [{"type": "text", "text": "京都でお勧めの観光地を教えて下さい"}]}]
}'),"$.content[0].text")) as response_from_bedrock\G
```

Let’s also look at how to summarize long texts stored in a database as our next example.

### Use case 2: Summarize existing data with Amazon Bedrock

Using Amazon Bedrock to summarize long texts stored in the database makes them less complicated to read. With summarization, you can get an overview in a short time, and if necessary, you can read the original data in the details. This use case has found application in summarizing product or service reviews and in summarizing case notes for support agents.

In this use case, we retrieve news about the latest releases of AWS services from What’s New with AWS?, then store it in the database, and retrieve only the product name from the saved data. We also summarize the release note. The table definition is provided in the GitHub repository.

Complete the following steps:

1. Create a sample table for storing data: 
1. Insert sample data by running the following script from other terminal (requires Python 3.7 or higher; you can run it using “python3 feed.py”. ):    
1. Create a procedure to add product names only from the description column: 
1. Run the procedure to get product name from description column by using Amazon Bedrock: 
1. After you run the procedure, you can confirm that the data has been added to the product column. This makes it more straightforward to understand the content. 
1. Create a procedure to add the summary of the description column to the summary column: 
1. Run the procedure to get summary data from Amazon Bedrock: 
1. After you run the procedure, you can confirm that the data has been add to the summary column: 
1. In the following example, you can also check the number of characters in the description and summary columns: 
By using group_concat, it’s also possible to create a summary by combining multiple data. The following output is an example of getting data from 20 rows and creating a summary. The sample code is provided in the GitHub repository:

```plain text
set session group_concat_max_len = 1048576;
set session aurora_ml_inference_timeout = 30000;
set @all = (select group_concat(description) from t_feed order by id desc limit 20);
set @question = concat('\"messages\": [{\"role\": \"user\",\"content\": [{\"type\": \"text\", \"text\": \" Please categorize and tell me what kind of services improvement being talked about based on the following content. ', @all,' ?\"}]}]}\'),\"$.content[0].text\")) as response_from_bedrock');
set @parameter = '(\'{\"anthropic_version\": \"bedrock-2023-05-31\",\"max_tokens\": 1024,\"temperature\": 0,\"top_p\": 0, \"top_k\":1, \"stop_sequences\": [],';
set @request = concat("select json_unquote(json_extract(claude3_haiku",@parameter,@question);

PREPARE select_stmt FROM @request;
EXECUTE select_stmt\G
DEALLOCATE PREPARE select_stmt;
```

## Considerations

Although the demonstration shows a response within a minute when running SQL commands, this can vary depending on the granularity and volume of the context. It’s important to adapt this proof of concept to your own implementation before deploying it to production. If you plan to perform large amounts of processing, we also recommend that you refer to Quotas for Amazon Bedrock and Amazon Bedrock Pricing for costs.

## Clean up

If you don’t need to use any of the resources you created, delete them when you are finished:

1. Drop unnecessary objects and users from the database.
1. If you no longer need to use Aurora ML but want to continue using your cluster, you can remove the ML related parameter (aws_default_bedrock_role) and IAM roles from you cluster.
1. If you no longer need the IAM role you created to access Amazon Bedrock, you can remove it and you may need to update some of your networking configurations.
1. If you no longer need your Aurora cluster, follow the instructions in Deleting Aurora DB clusters and DB instances.
## Conclusion

Businesses today want to enhance the data stored in their relational databases with generative AI FMs to improve the end-user experience or improve productivity. In this post, we demonstrated how to obtain supplemental information for stored data using Amazon Bedrock. We also demonstrated how you can summarize the document stored in an Aurora database by using the Aurora ML integration capabilities with Amazon Bedrock.

The ability to invoke FMs on Amazon Bedrock as SQL functions using Aurora ML simplifies the learning curve in using LLMs while building generative AI applications. It provides straightforward, optimized, and secure integration between Aurora and AWS ML services without having to build custom integrations or move data around.

For more information about Aurora ML, see Amazon Aurora Machine Learning. To explore the latest in Aurora ML with Amazon Aurora MySQL refer to Using Amazon Aurora machine learning with Aurora MySQL.

We invite you to leave feedback in the comments.

### About the Authors

Steve Dille is a Senior Product Manager for Amazon Aurora. He leads all generative AI strategy and product initiatives with Aurora databases for AWS. Previous to this role, Steve founded the performance and benchmark team for Aurora and then built and launched the RDS Data API for Amazon Aurora Serverless v2. He has been with AWS for 4 years. Prior to this, he served as a software developer at NCR, product manager at HP and Data Warehousing Director at Sybase (SAP). He has over 20 years of experience as VP of Product or CMO on the executive teams of companies resulting in five successful company acquisitions and one IPO in the data management, analytics, and big data sectors. Steve earned a Master’s in Information and Data Science at UC Berkeley, an MBA from the University of Chicago Booth School of Business and a BS in Computer Science/Math with distinction from University of Pittsburgh.


