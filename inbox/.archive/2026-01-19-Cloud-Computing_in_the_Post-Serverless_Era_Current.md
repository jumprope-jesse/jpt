---
type: link
source: notion
url: https://www.infoq.com/articles/cloud-computing-post-serverless-trends/
notion_type: Product Website
tags: 
created: 2024-01-24T05:09:00.000Z
---

# Cloud-Computing in the Post-Serverless Era: Current Trends and Beyond

## AI Summary (from Notion)
- Evolution of Serverless Computing: Serverless technology is moving beyond just Function as a Service (FaaS) to encompass broader cloud services that require no manual provisioning and offer on-demand scalability.

- Shift from Functions to Constructs: There's a transition from using functions to employing configurable cloud constructs that simplify application development, such as request routing and data transformation without needing to write extensive function code.

- Emergence of Hyperspecialized Services: The cloud landscape is shifting towards vertical multi-cloud services that excel in specific areas, providing more granular developer constructs and enhancing the developer experience.

- From Infrastructure as Code to Composition as Code: The evolution in cloud management is moving from Infrastructure as Code (IaC) to using general-purpose programming languages for defining cloud constructs, leading to a more dynamic and developer-friendly environment.

- Integration of Programming Constructs: Cloud services are increasingly integrating programming constructs, allowing for more intuitive configuration and management of cloud applications, reducing code complexity and maintenance needs.

- Impact on Microservices: Microservices are being redefined, transitioning from simple architectural boundaries to more complex organizational constructs that incorporate various cloud capabilities.

- Future Trends: Upcoming trends include the development of construct-rich cloud services and the continued blending of application programming with cloud service configuration, leading to a more developer-centric approach in cloud computing.

- Significant Players: Notable examples of specialized services include Confluent Cloud for Kafka, Vercel for frontend development, and Supabase as an alternative to Firebase, showcasing the shift towards niche expertise in the cloud market.

## Content (from Notion)

Feed your curiosity. Help 550k+ global senior developers each month stay ahead.Get in touch

### Key Takeaways

- Serverless computing is evolving beyond its original scope, with functions partially or fully replaced by versatile cloud constructs, heralding a new era in cloud architecture.
- The cloud market is shifting toward hyperspecialized vertical multi-cloud services, offering unique, fine-grained features that cater specifically to developers’ needs.
- Upcoming cloud services are set to be rich in constructs, transforming the way developers handle tasks like routing, filtering, and event-triggering, making them more efficient and user-friendly.
- There’s a significant trend moving from Infrastructure as Code to Composition as Code, where developers use familiar programming languages for more intuitive cloud-service configuration.
- Microservices are being redefined in the cloud landscape, evolving from mere architectural boundaries to organizational boundaries, integrating various cloud constructs under a unified developer language.
[Note: The opinions and predictions in this article are those of the author and not of InfoQ.]

As AWS Lambda approaches its 10th anniversary this year, serverless computing expands beyond just Function as a Service (FaaS). Today, serverless describes cloud services that require no manual provisioning, offer on-demand auto-scaling, and use consumption-based pricing. This shift is part of a broader evolution in cloud computing, with serverless technology continuously transforming. This article focuses on the future beyond serverless, exploring how the cloud landscape will evolve beyond current hyperscaler models and its impact on developers and operations teams. I will examine the top three trends shaping this evolution.

## From Primitives to Constructs as a Service

In software development, a "module" or "component" typically refers to a self-contained unit of software that performs a cohesive set of actions. This concept corresponds elegantly to the microservice architecture that typically runs on long-running compute services such as Virtual Machines (VMs) or a container service. AWS EC2, one of the first widely accessible cloud computing services, offered scalable VMs. Introducing such scalable, accessible cloud resources provided the infrastructure necessary for microservices architecture to become practical and widespread. This shift led to decomposing monolithic applications into independently deployable microservice units.

### Related Sponsored Content

### Related Sponsor

The true promise of the cloud with ease, not cost. DoiT provides technology and cloud expertise to reduce cloud costs and boost engineer productivity. All from an AWS, Microsoft and Google Cloud Partner. Learn More.

Let’s continue with this analogy of software units. A function is a block of code that encapsulates a sequence of statements performing a single task with defined input and output. This unit of code nicely corresponds to the FaaS execution model. The concept of FaaS executing code in response to events without the need to manage infrastructure existed before AWS Lambda but lacked broad implementation and recognition.

The concept of FaaS, which involves executing code in response to events without the need for managing infrastructure, was already suggested by services like Google App Engine, Azure WebJobs, IronWorker, and AWS Elastic Beanstalk before AWS Lambda brought it into the mainstream. Lambda, emerging as the first major commercial implementation of FaaS, acted as a catalyst for its popularity by easing the deployment process for developers. This advancement led to the transformation of microservices into smaller, individually scalable, event-driven operations.

In the evolution toward smaller software units offered as a service, one might wonder if we will see basic programming elements like expressions or statements as a service (such as int x = a + b;). The progression, however, steers away from this path. Instead, we are witnessing the minimization and eventual replacement of functions by configurable cloud constructs. Constructs in software development, encompassing elements like conditionals (if-else, switch statements), loops (for, while), exception handling (try-catch-finally), or user-defined data structures, are instrumental in controlling program flow or managing complex data types. In cloud services, constructs align with capabilities that enable the composition of distributed applications, interlinking software modules such as microservices and functions, and managing data flow between them.

Cloud construct replacing functions, replacing microservices, replacing monolithic applications

While you might have previously used a function to filter, route, batch, split events, or call another cloud service or function, now these operations and more can be done with less code in your functions, or in many cases with no function code at all. They can be replaced by configurable cloud constructs that are part of the cloud services. Let’s look at a few concrete examples from AWS to demonstrate this transition from Lambda function code to cloud constructs:

- Request routing - Rather than using Lambda to parse a request and route it to the right backend endpoint, API Gateway routes can do the routing. Not only that, but API Gateway also integrates with other AWS services, and it can call them directly, eliminating the need for a function.
- Request validation - API Gateway can validate the body, query string parameters, and headers using OpenAPI.
- Data transformation - API Gateway can use Apache Velocity templates to transform request and response data to override payload, parameters, headers, and status codes without Lambda.
- Streaming database changes - DynamoDB Streams emit all data changes. This becomes a mandatory construct for any data store removing the need for dual write from application code and any data polling code by turning microservices inside out.
- Event triggering - AWS Event Source Mapping allows triggering a Lambda by reading from an event source and invoking a Lambda function.
- Event filtering - Event Source Mapping can perform event filtering to control which records from a stream or queue to call your Lambda function. This eliminates the need to write filtering logic within our function and reduces its size and cost substantially.
- Event batching - In a similar manner, Event Source Mappings batch records together into a single payload before sending it to your function. There is no need to manually loop to aggregate events or to split them before processing.
- Event transformation - EventBridge Pipes can transform the data from the source using JSON path syntax before sending it to the target.
- Event enrichment - EventBridge Pipes can also call another endpoint to enrich a request before processing it further. This provides an implementation of the Content Enricher pattern that can be used fully declaratively.
- Event routing - Similarly to request routing, EventBridge rules can perform event routing, allowing you to offload this responsibility from your application code and eliminate Lambda functions.
- Result-based routing - Lambda Destination allows asynchronous invocations to route the execution results to other AWS services, replacing the Lambda invocation code with configuration code.
- Calling other services - StepFunction tasks don’t require a Lambda function to call other services or external HTTP endpoints. With that, the StepFunction task definition can, for example, perform HTTP calls or read, update, and delete database records without a Lambda function.
These are just a few examples of application code constructs becoming serverless cloud constructs. Rather than validating input values in a function with if-else logic, you can validate the inputs through configuration. Rather than routing events with a case or switch statement to invoke other code from within a function, you can define routing logic declaratively outside the function. Events can be triggered from data sources on data change, batched, or split without a repetition construct, such as a for or while loop.

Events can be validated, transformed, batched, routed, filtered, and enriched without a function. Failures were handled and directed to DLQs and back without a try-catch code, and successful completion was directed to other functions and service endpoints. Moving these constructs from application code into construct configuration reduces application code size or removes it, eliminating the need for security patching and any maintenance.

A primitive and a construct in programming have distinct meanings and roles. A primitive is a basic data type inherently part of a programming language. It embodies a basic value, such as an integer, float, boolean, or character, and does not comprise other types. Mirroring this concept, the cloud - just like a giant programming runtime - is evolving from infrastructure primitives like network load balancers, virtual machines, file storage, and databases to more refined and configurable cloud constructs.

Like programming constructs, these cloud constructs orchestrate distributed application interactions and manage complex data flows. However, these constructs are not isolated cloud services; there isn’t a standalone "filtering as a service" or "event emitter as service." There are no "Constructs as a Service," but they are increasingly essential features of core cloud primitives such as gateways, data stores, message brokers, and function runtimes.

This evolution reduces application code complexity and, in many cases, eliminates the need for custom functions. This shift from FaaS to NoFaaS (no fuss, implying simplicity) is just beginning, with insightful talks and code examples on GitHub. Next, I will explore the emergence of construct-rich cloud services within vertical multi-cloud services.

## From Hyperscale to Hyperspecialization

In the post-serverless cloud era, it’s no longer enough to offer highly scalable cloud primitives like compute for containers and functions, or storage services such as key/value stores, event stores, relational databases, or networking primitives like load balancers. Post-serverless cloud services must be rich in developer constructs and offload much of the application plumbing. This goes beyond hyperscaling a generic cloud service for a broad user base; it involves deep specialization and exposing advanced constructs to more demanding users.

Hyperscalers like AWS, Azure, GCP, and others, with their vast range of services and extensive user bases, are well-positioned to identify new user needs and constructs. However, providing these more granular developer constructs results in increased complexity. Each new construct in every service requires a deep learning curve with its specifics for effective utilization. Thus, in the post-serverless era, we will observe the rise of vertical multi-cloud services that excel in one area. This shift represents a move toward hyperspecialization of cloud services.

Consider Confluent Cloud as an example. While all major hyperscalers (AWS, Azure, GCP, etc.) offer Kafka services, none match the developer experience and constructs provided by Confluent Cloud. With its Kafka brokers, numerous Kafka connectors, integrated schema registry, Flink processing, data governance, tracing, and message browser, Confluent Cloud delivers the most construct-rich and specialized Kafka service, surpassing what hyperscalers offer.

This trend is not isolated; numerous examples include MongoDB Atlas versus DocumentDB, GitLab versus CodeCommit, DataBricks versus EMR, RedisLabs versus ElasticCache, etc. Beyond established cloud companies, a new wave of startups is emerging, focusing on a single multi-cloud primitive (like specialized compute, storage, networking, build-pipeline, monitoring, etc.) and enriching it with developer constructs to offer a unique value proposition. Here are some cloud services hyperspecializing in a single open-source technology, aiming to provide a construct-rich experience and attract users away from hyperscalers:

- Vercel: Renowned for its exceptional frontend developer experience, streamlining web application deployment.
- Railway: Distinguished for enhancing backend developer experience with straightforward deployment and scaling management.
- Supabase: An open-source alternative to Firebase, providing similar functionalities with more flexibility.
- Fauna: A serverless database known for declarative relational queries and functional business logic in strongly consistent transactions.
- Neon: Offers the simplest serverless PostgreSQL, with features like database branching and minimal management overhead.
- PlanetScale: Known for advanced MySQL cloud services, focusing on development-friendly features.
- PolyScale: Specializes in AI-driven caching to optimize data performance through intelligent caching.
- Upstash: Provides a fully-managed, low-latency serverless Kafka solution suitable for event streaming.
- Diagrid Catalyst: Delivers serverless Dapr APIs for messaging, data, and workflows, acting as a connective tissue between cloud services.
- Temporal: Provides durable execution, offering a platform for reliably managing complex workflows.
This list represents a fraction of a growing ecosystem of hyperspecialized vertical multi-cloud services built atop core cloud primitives offered by hyperscalers. They compete by providing a comprehensive set of programmable constructs and an enhanced developer experience.

Serverless cloud services hyperspecializing in one thing with rich developer constructs

Once this transition is completed, bare-bones cloud services without rich constructs, even serverless ones, will seem like outdated on-premise software. A storage service must stream changes like DynamoDB; a message broker should include EventBridge-like constructs for event-driven routing, filtering, and endpoint invocation with retries and DLQs; a pub/sub system should offer message batching, splitting, filtering, transforming, and enriching.

Ultimately, while hyperscalers expand horizontally with an increasing array of services, hyperspecializers grow vertically, offering a single, best-in-class service enriched with constructs, forming an ecosystem of vertical multi-cloud services. The future of cloud service competition will pivot from infrastructure primitives to a duo of core cloud primitives and developer-centric constructs.

## From Infrastructure to Composition as Code(CaC)

Cloud constructs increasingly blur the boundaries between application and infrastructure responsibilities. The next evolution is the "shift left" of cloud automation, integrating application and automation codes in terms of tools and responsibilities. Let’s examine how this transition is unfolding.

The first generation of cloud infrastructure management was defined by Infrastructure as Code (IaC), a pattern that emerged to simplify the provisioning and management of infrastructure. This approach is built on the trends set by the commoditization of virtualization in cloud computing.

The initial IaC tools introduced new domain-specific languages (DSL) dedicated to creating, configuring, and managing cloud resources in a repeatable manner. Tools like Chef, Ansible, Puppet, and Terraform led this phase. These tools, leveraging declarative languages, allowed operation teams to define the infrastructure’s desired state in code, abstracting underlying complexities.

However, as the cloud landscape transitions from low-level coarse-grained infrastructure to more developer-centric programmable finer-grained constructs, a trend toward using existing general-purpose programming languages for defining these constructs is emerging. New entrants like Pulumi and the AWS Cloud Development Kit (CDK) are at the forefront of this wave, supporting languages such as TypeScript, Python, C#, Go, and Java.

The shift to general-purpose languages is driven by the need to overcome the limitations of declarative languages, which lack expressiveness and flexibility for programmatically defining cloud constructs, and by the shift-left of configuring cloud constructs responsibilities from operations to developers. Unlike the static nature of declarative languages suited for low-level static infrastructure, general-purpose languages enable developers to define dynamic, logic-driven cloud constructs, achieving a closer alignment with application code.

Shifting-left of application composition from infrastructure to developer teams

The post-serverless cloud developers need to implement business logic by creating functions and microservices but also compose them together using programmable cloud constructs. This shapes a broader set of developer responsibilities to develop and compose cloud applications. For example, a code with business logic in a Lambda function would also need routing, filtering, and request transformation configurations in API Gateway.

Another Lambda function may need DynamoDB streaming configuration to stream specific data changes, EventBridge routing, filtering, and enrichment configurations.

A third application may have most of its orchestration logic expressed as a StepFunction where the Lambda code is only a small task. A developer, not a platform engineer or Ops member, can compose these units of code together. Tools such as Pulumi, AWS SDK, and others that enable a developer to use the languages of their choice to implement a function and use the same language to compose its interaction with the cloud environment are best suited for this era.

Platform teams still can use declarative languages, such as Terraform, to govern, secure, monitor, and enable teams in the cloud environments, but developer-focused constructs, combined with developer-focused cloud automation languages, will shift left the cloud constructs and make developer self-service in the cloud a reality.

The transition from DSL to general-purpose languages marks a significant milestone in the evolution of IaC. It acknowledges the transition of application code into cloud constructs, which often require a deeper developer control of the resources for application needs. This shift represents a maturation of IaC tools, which now need to cater to a broader spectrum of infrastructure orchestration needs, paving the way for more sophisticated, higher-level abstractions and tools.

The journey of infrastructure management will see a shift from static configurations to a more dynamic, code-driven approach. This evolution hasn’t stopped at Infrastructure as Code; it is transcending into a more nuanced realm known as Composition as Code. This paradigm further blurs the lines between application code and infrastructure, leading to more streamlined, efficient, and developer-friendly practices.

## Summary

In summarizing the trends and their reinforcing effects, we’re observing an increasing integration of programming constructs into cloud services. Every compute service will integrate CI/CD pipelines; databases will provide HTTP access from the edge and emit change events; message brokers will enhance capabilities with filtering, routing, idempotency, transformations, DLQs, etc.

Infrastructure services are evolving into serverless APIs, infrastructure inferred from code (IfC), framework-defined infrastructure, or explicitly composed by developers (CaC). This evolution leads to smaller functions and sometimes to NoFaaS pattern, paving the way for hyperspecialized, developer-first vertical multi-cloud services. These services will offer infrastructure as programmable APIs, enabling developers to seamlessly merge their applications using their preferred programming language.

The shift-left of application composition using cloud services will increasingly blend with application programming, transforming microservices from an architectural style to an organizational one. A microservice will no longer be just a single deployment unit or process boundary but a composition of functions, containers, and cloud constructs, all implemented and glued together in a single language chosen by the developer. The future is shaping to be hyperspecialized and focused on the developer-first cloud.


