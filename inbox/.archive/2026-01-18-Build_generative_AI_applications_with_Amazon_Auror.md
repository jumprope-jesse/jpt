---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/build-generative-ai-applications-with-amazon-aurora-and-knowledge-bases-for-amazon-bedrock/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-30T03:58:00.000Z
---

# Build generative AI applications with Amazon Aurora and Knowledge Bases for Amazon Bedrock | AWS Database Blog

## AI Summary (from Notion)
- Generative AI Applications: The document discusses building generative AI applications using Amazon Aurora and Knowledge Bases for Amazon Bedrock, emphasizing the ease of integrating foundational models with private data.

- Retrieval Augmented Generation (RAG): RAG is highlighted as a technique that augments foundational model responses with relevant company data, enhancing accuracy and personalization.

- Amazon Aurora: Aurora is presented as a high-performance database solution that can significantly improve vector similarity searches, offering up to 20 times faster queries with pgvector.

- Knowledge Bases for Amazon Bedrock: This feature automates the RAG workflow, allowing seamless integration of private data for customized responses without the need for extensive coding.

- Aurora ML Integration: The integration of Amazon Bedrock with Aurora ML enables users to generate embeddings directly from SQL commands, simplifying the process of creating AI applications.

- Setup Instructions: Detailed instructions are provided for setting up an Aurora PostgreSQL cluster, configuring an S3 bucket, and creating a knowledge base within Amazon Bedrock.

- IAM Roles: The necessity of creating IAM roles and policies for secure communication between Aurora and Bedrock is emphasized, ensuring that the Aurora cluster can invoke models in Amazon Bedrock.

- Batch Processing for Embeddings: The document illustrates how to efficiently generate embeddings in bulk using Aurora ML, optimizing performance and reducing latency.

- Cleanup Recommendations: It advises users to delete unused resources post-project completion to maintain cost-effectiveness and resource management.

- Author Background: The document concludes with information about the author, Steve Dille, highlighting his expertise and experience in product management for AWS RDS Aurora and generative AI strategies.

## Content (from Notion)

Amazon Bedrock is the easiest way to build and scale generative AI applications with foundational models (FMs). FMs are trained on vast quantities of data, allowing them to be used to answer questions on a variety of subjects. However, if you want to use an FM to answer questions about your private data that you have stored in your Amazon Simple Storage Service (Amazon S3) bucket or Amazon Aurora PostgreSQL-Compatible Edition database, you need to use a technique known as Retrieval Augmented Generation (RAG) to provide relevant answers for your customers.

Knowledge Bases for Amazon Bedrock is a fully managed RAG capability that allows you to customize FM responses with contextual and relevant company data. Knowledge Bases for Amazon Bedrock automates the end-to-end RAG workflow, including ingestion, retrieval, prompt augmentation, and citations, eliminating the need for you to write custom code to integrate data sources and manage queries.

Integrating Amazon Bedrock with Amazon Aurora PostgreSQL lets you utilize features that help accelerate performance of vector similarity search for RAG. Aurora delivers queries 20 times faster with pgvector’s HNSW indexing over other indexing methods. Additionally, Amazon Aurora Optimized Reads can increase performance for vector search with pgvector by up to nine times for workloads that exceed regular instance memory. This is on top of the performance and availability features that let you operate Aurora cost-effectively at global scale, including Aurora Serverless and Amazon Aurora Global Database.

In this post, we explore how to use Amazon Aurora to build generative AI applications using RAG. We walk through setting up an Aurora cluster to be a knowledge base for Amazon Bedrock. We also demonstrate how to use the Amazon Aurora Machine Learning extension to generate embeddings using Amazon Bedrock from simple SQL commands.

## Solution overview

The following diagram illustrates an example of a RAG workflow.

The RAG workflow contains two parts. The first part is taking unstructured data, such as text, images, and video, converting it into embeddings (vectors) using an embeddings model, and storing it in a vector database (Steps 1–3). An embedding is a numerical representation that you can use in a similarity search to find content that is most related to a query. The second part of the workflow is the request itself. The request is turned into an embedding and used to query the vector database to find content to augment the prompt (Steps 4–5). The output of the query is sent to the FM, which then sends the response to the user (Steps 6–7). Building a generative AI application that uses RAG requires orchestrating this workflow, which can require additional work beyond building the application logic.

Recently, AWS announced the general availability of Knowledge Bases for Amazon Bedrock. With Knowledge Bases for Amazon Bedrock, you can give FMs and agents contextual information from your company’s private data sources for RAG to deliver more relevant, accurate, and customized responses. You can then use your knowledge base with Agents for Amazon Bedrock to orchestrate multi-step tasks and facilitate prompt engineering. For more information, refer to Knowledge Bases now delivers fully managed RAG experience in Amazon Bedrock.

In the following sections, we demonstrate how to set up Aurora as a knowledge base for Amazon Bedrock. We’ll also see how to use Aurora Machine Learning (ML) to generate embeddings using SQL commands.

## Prerequisites

This post assumes familiarity with navigating the AWS Management Console. For this example, you’ll also need the following resources and services enabled in your AWS account:

- An Aurora PostgreSQL cluster with Aurora ML enabled
- The RDS Data API enabled for the Aurora cluster
- Amazon S3
- AWS Secrets Manager
- AWS Identity and Access Management (IAM)
- Amazon Bedrock. You may need to request access to use specific foundational models in Amazon Bedrock. In this blog post, we used Anthropic Claude 2.1 and Amazon Titan Embeddings G1 – Text.
## Set up Aurora as a knowledge base for Amazon Bedrock

The first step to creating a knowledge base for Amazon Bedrock is to have content that can be used to augment a foundation model. In this example, we use a PDF version of the PostgreSQL 16 manual. At the time of writing, PostgreSQL 16 was a new release and was not available for FM training on public data. Datasets used in RAG often have much more data, but we chose to keep this example simple.

### Configure an S3 bucket

To begin setting up a knowledge base for Amazon Bedrock, you’ll need to create an S3 bucket. Make sure this bucket is private. This example uses a bucket called bedrock-kb-demo-aurora. After you create the bucket, upload the PostgreSQL 16 manual to the bucket. The following screenshot shows what the upload looks like when it’s complete.

### Configure an Aurora PostgreSQL cluster

Next, create an Aurora PostgreSQL cluster. For full instructions, refer to Using Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock. We highlight a few specific configuration options used in this example:

1. On the Aurora console, create a new cluster.
1. For Engine options¸ select Aurora (PostgreSQL Compatible).
1. For Engine version, choose your engine version.
We selected PostgreSQL 15.5 for this example; we recommend using PostgreSQL 15.5 or higher so you can use the latest version of the open source pgvector extension.

1. For Configuration options, select either Aurora Standard or Aurora I/O Optimized.
We selected Aurora I/O-Optimized, which provides improved performance with predictable pricing for I/O-intensive applications.

1. For DB instance class, select your instance class.
We opted to use Amazon Aurora Serverless v2, which automatically scales your compute based on your application workload, so you only pay based on the capacity used.

1. Enable the RDS Data API, which is used by Amazon Bedrock to access your Aurora cluster.
1. Create your Aurora cluster.
1. While your Aurora cluster is provisioning, navigate to the cluster on the Aurora console and choose the Configuration tab.
1. Note the Amazon Resource Name (ARN) for the cluster, and save it for later.
You’ll need the ARN for configuring the knowledge base for Amazon Bedrock.

It takes about 10 minutes for the Aurora PostgreSQL cluster to finish provisioning. After the cluster is provisioned, you need to run a series of SQL commands to prepare your cluster to be a knowledge base.

1. Log in to your Aurora cluster either as the admin user (for example, postgres) or a user that has the rds_superuser privilege, and run the following code. Note the password that you create for bedrock_user, because you’ll need it in a later step when configuring a secret in Secrets Manager. Also note the table names and column names, because they’ll be used in the knowledge base workflow on the Amazon Bedrock console. 
The Aurora cluster is now set up to be used as a knowledge base for Amazon Bedrock. We’ll now create a secret in Secrets Manager that Amazon Bedrock will use to connect to the cluster.

## Create a secret in Secrets Manager

Secrets Manager lets you store your Aurora credentials so that they can be securely transmitted to applications. Complete the following steps to create your secret:

1. On the Secrets Manager console, create a new secret.
1. For Secret type, select Credentials for Amazon RDS database.
1. Under Credentials, enter a name for your user (for this post, we use bedrock_user) and the password for that role.
1. In the Database section, select the cluster you’re using for the knowledge base.
1. Choose Next.
1. For Secret name, enter a name for your secret.
1. Choose Next.
1. Finish creating the secret and copy the secret ARN.
You’ll need the secret ARN for creating your knowledge base.

We’re now ready to use this Aurora cluster as a knowledge base for Amazon Bedrock.

## Create a knowledge base for Amazon Bedrock

We can now use our cluster as a knowledge base. Complete the following steps:

1. On the Amazon Bedrock console, choose Knowledge base under Orchestration in the navigation pane.
1. Choose Create knowledge base.
1. For Knowledge base name¸ enter a name.
1. For Runtime role, select Create and use a new service role and enter a service role name.
1. Choose Next.
1. For Choose an archive in S3, select the S3 bucket to use as a data source and choose Choose.
For this post, we use the S3 bucket containing the PostgreSQL 16 manual that we uploaded earlier.

1. For Embeddings model, select your model (for this post, we use Amazon Titan Embeddings G1 – Text).
1. For Vector database, select Choose a vector store you have created and select Amazon Aurora.
1. Provide the following additional information (note the examples we use for this post): 
1. Choose Next.
1. Review the summary page and choose Sync.
This begins the process of converting the unstructured data stored in the S3 bucket into embeddings and storing them in your Aurora cluster.

The syncing operation may take minutes to hours to complete, based on the size of the dataset stored in your S3 bucket. During the sync operation, Amazon Bedrock downloads documents in your S3 bucket, divides them into chunks (we opt for the “default” strategy in this post), generates the vector embedding, and stores the embedding in your Aurora cluster. When the initial sync is complete, you’ll see that the data source shows as Ready.

Now you can use your knowledge base as in an agent for Amazon Bedrock. We can use this knowledge base as part of a test. For this example, we chose the PostgreSQL 16 manual as our dataset. This lets us see how RAG works in action, because foundational models may not yet have information on all the features of PostgreSQL 16.

In the following example, we use the Test knowledge base feature of Amazon Bedrock, choose the Anthropic Claude 2.1 model, and ask it a question about a PostgreSQL 16 feature—specifically, the pg_stat_io view. The following screenshot shows our answer.

Using the provided question, Amazon Bedrock queried our Aurora cluster to get the additional context needed to answer the question. Our knowledge base contained information on how the new pg_stat_io feature works, and was able to provide an augmented answer via Anthropic Claude. The test tool also cites the chunks it uses to provide attribution to how it delivered its response.

Now that we’ve seen how we can augment foundational model responses with knowledge bases for Amazon Bedrock and an Aurora PostgreSQL cluster, let’s learn how we can generate embeddings directly from an Aurora cluster. This will be necessary to convert user questions into embeddings that can be compared to embeddings in Aurora with similarity search.

## Create an IAM role and policy for the Aurora cluster

Before you can start generating vector embeddings from Amazon Bedrock directly from Aurora, you may need to adjust the network configuration so your Aurora cluster can communicate with Amazon Bedrock. For more information on how to do this, see Enabling network communication from Amazon Aurora MySQL to other AWS services. These directions also apply to Aurora PostgreSQL clusters.

To allow Aurora ML to work with Amazon Bedrock, you must first create an IAM policy that allows the Aurora cluster to communicate with Amazon Bedrock models. Complete the following steps:

1. On the IAM console, choose Policies in the navigation pane, then choose Create policy.
1. In the policy editor, expand Bedrock and under Read, select InvokeModel to allow that action.
1. Expand Resources and select Specific.
1. For foundation-model, select Any. As a best practice, make sure to only give access to the foundational models in Amazon Bedrock that your team requires.
1. For provisioned-model, select Any in this account. As a best practice, make sure to only give access to provisioned models in Amazon Bedrock that your team requires.
1. Choose Next.
1. For Policy name, enter a name for your policy, such as AuroraMLBedrock.
1. Choose Create policy.
1. On the IAM console, choose Roles in the navigation pane, then choose Create role.
1. For Trusted entity type, select AWS service.
1. For Service or use case, choose RDS.
1. Select RDS – Add Role to Database.
1. Choose Next.
Now we assign the IAM policy we created in the previous step to this IAM role.

1. For Permission policies, find and select the AuroraMLBedrock policy.
1. Choose Next.
1. In the Role details section, enter a name (for this post, AuroraMLBedrock) and a description.
1. Review the IAM role and confirm that the AuroraMLBedrock policy is attached.
1. Choose Create to create the role.
Now we need to assign the AuroraMLBedrock IAM role to the Aurora cluster.

1. On the Amazon RDS console, navigate to your Aurora cluster details page.
1. On the Connectivity & security tab, locate the Manage IAM roles section.
1. For Add IAM roles to this cluster, choose the AuroraMLBedrock role.
1. For Feature, choose Bedrock.
1. Choose Add role.
Your cluster can now invoke models in Amazon Bedrock.

## Use Aurora ML to generate vector embeddings

Aurora machine learning is an Aurora feature that lets builders work directly with AWS ML services using SQL commands, including Amazon Bedrock, Amazon SageMaker, and Amazon Comprehend. With recent support for Amazon Bedrock, Aurora ML gives you access to foundational models and embedding generators, helping reduce latency when working with data already stored in you Aurora cluster. This includes two new functions: aws_bedrock.invoke_model, which lets you use a foundational model from a SQL query, and aws_bedrock.invoke_model_get_embeddings, which lets you generate an embedding from a SQL query. For more information, see Using Amazon Aurora machine learning with Aurora PostgreSQL.

Let’s see how we can use Aurora ML to generate an embedding from Amazon Bedrock. First, log in as an account with the rds_superuser privilege (for example, postgres) to your Aurora cluster and install the Aurora ML extension in your database:

```plain text
CREATE EXTENSION IF NOT EXISTS aws_ml CASCADE;
```

You should see the following output:

```plain text
CREATE EXTENSION
```

You can now create embeddings directly from Aurora. The following example shows how to generate an embedding using the Titan Embeddings G1 – Text embedding model for the phrase “PostgreSQL I/O monitoring views”:

```plain text
SELECT aws_bedrock.invoke_model_get_embeddings(
   model_id      := 'amazon.titan-embed-text-v1',
   content_type  := 'application/json',
   json_key      := 'embedding',
   model_input   := '{ "inputText": "PostgreSQL I/O monitoring views"}') AS embedding;
```

You should see the following output (abbreviated for clarity):

```plain text
 {-1.0625,-1.1484375,0.578125,-0.08251953,0.39453125,-0.80859375,0.051513672,-0.0016479492,-1.203125,0.49609375,-0.33984375 ... -0.37695312,-0.16699219,-0.796875,1.21875,-0.36523438 }
```

You can use the aws_bedrock.invoke_model_get_embeddings function to generate embeddings from data that already exists in your database. However, because calling an embedding model on a single input can take 100–400 milliseconds to complete, you should use PostgreSQL’s stored procedure system on a batch query to prevent a single long-running transaction from blocking other processes.

The following example shows how we can add embeddings to an existing table and manage the batch import using an anonymous block. First, make sure the pgvector extension is installed in the database and create a table that will contain example data:

```plain text
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE documents (
  id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  content text NOT NULL,
  embedding vector(1536)
);
INSERT INTO documents (content)
VALUES
  ('Allow parallelization of FULL and internal right OUTER hash joins'),
  ('Allow logical replication from standby servers'),
  ('Allow logical replication subscribers to apply large transactions in parallel'),
  ('Allow monitoring of I/O statistics using the new pg_stat_io view'),
  ('Add SQL/JSON constructors and identity functions'),
  ('Improve performance of vacuum freezing'),
  ('Add support for regular expression matching of user and database names in pg_hba.conf, and user names in pg_ident.conf');
```

Now you can generate embeddings for this dataset in bulk using the following code. The example code loops through all of the records in the documents table that don’t have an embedding. For each record, the code calls the Amazon Titan embedding model to generate the embedding, and updates and commits the result to the database.

```plain text
DO
$embed$
    DECLARE
        doc RECORD;
        emb vector(1536);
    BEGIN
        FOR doc in SELECT id, content FROM documents WHERE embedding IS NULL LOOP
            EXECUTE $$ SELECT aws_bedrock.invoke_model_get_embeddings(
                    model_id      := 'amazon.titan-embed-text-v1',
                    content_type  := 'application/json',
                    json_key      := 'embedding',
                    model_input   := json_build_object('inputText', $1)::text)$$
                INTO emb
                USING doc.content;
            UPDATE documents SET embedding = emb WHERE id = doc.id;
            COMMIT;
        END LOOP;
    END;
$embed$ LANGUAGE plpgsql;
```

In this section, we saw how to use Aurora ML to generate embeddings using Amazon Bedrock from data that already exists in your Aurora database. This technique helps speed up creating embeddings from the data in your database, because you can reduce latency by calling Amazon Bedrock directly without first transferring to a separate system.

## Clean up

If you don’t need to use any of the resources you created, delete them when you are finished:

1. Empty and delete your S3 bucket.
1. If you no longer need to use the Aurora ML extension but would like to continue using your cluster, you can remove it from your Aurora cluster by running the following SQL command: 
1. Additionally, if you no longer need to use the Aurora ML extension but would like to continue using your Aurora cluster, you can remove the IAM role you created to access Amazon Bedrock from your cluster, and you may need to update some of your networking configurations.
1. To delete your knowledge base, refer to Manage your knowledge base.
1. If you no longer need your Aurora cluster, follow the instructions in Deleting Aurora DB clusters and DB instances.
## Conclusion

RAG is a powerful technique that lets you combine domain-specific information with a FM to enrich responses in your generative AI applications. In this post, we covered multiple examples for how you can use Amazon Bedrock with Aurora to implement RAG for your generative AI applications. This included how to set up Amazon Aurora PostgreSQL as a knowledge base for Amazon Bedrock, and how to use Aurora ML to generate vector embeddings from Amazon Bedrock.

To learn more about using Amazon Aurora PostgreSQL and pgvector for AI and ML workloads, see Leverage pgvector and Amazon Aurora PostgreSQL for Natural Language Processing, Chatbots and Sentiment Analysis.

We invite you to leave feedback in the comments.

### About the Authors

Steve Dille is a Senior Product Manager for RDS Aurora, he leads all generative AI strategy and product initiatives with Aurora databases for AWS. Previous to this role, Steve founded the performance and benchmark team for Aurora and then built and launched RDS Data API for Aurora Serverless v2. He has been with AWS for 4 years. Prior to this, he served as a software developer at NCR, product manager at HP, Data Warehousing Director at Sybase (SAP). He has over 20 years of experience as VP of Product or CMO on the executive teams of companies resulting in 5 successful company acquisitions and one IPO in the data management, analytics, and big data sectors. Steve earned a Master’s in Information and Data Science at UC Berkeley, MBA from the University of Chicago Booth School of Business and a BS in Computer Science/Math with distinction from University of Pittsburgh.


