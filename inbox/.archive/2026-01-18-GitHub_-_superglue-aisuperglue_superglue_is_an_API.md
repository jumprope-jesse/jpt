---
type: link
source: notion
url: https://github.com/superglue-ai/superglue
notion_type: Software Repo
tags: ['Running']
created: 2025-02-27T19:02:00.000Z
---

# GitHub - superglue-ai/superglue: superglue is an API connector that writes its own code. It lets you connect to any API/data source and get the data you want in the format you need.

## Overview (from Notion)
- Superglue's API connector can streamline your workflow, saving time on integration tasks and allowing you to focus on more strategic aspects of your projects.
- The ability to translate data into the desired format can enhance your product offerings, providing better user experiences for clients or customers.
- Leveraging self-healing and fast deployment features may help you stay ahead in a competitive market, keeping your tech stack agile and responsive to changes.
- Open-source nature allows for customization, letting you tailor the tool to fit specific needs of your business or projects.
- Consider the ethical implications of using AI in data processing and ensure compliance with data protection regulations, especially when handling sensitive information.
- The community aspect of open-source tools can provide networking opportunities and insights from other developers facing similar challenges.
- Balancing automation with human oversight is crucial; while tools like Superglue can enhance productivity, maintaining a personal touch in customer interactions is vital.
- Explore how such technology can facilitate family-oriented projects, perhaps enabling you to create educational tools or experiences for your children.

## AI Summary (from Notion)
Superglue is an open-source API connector that automates data extraction, mapping, and transformation, allowing developers to easily integrate various data sources without complex coding. It features LLM-powered translations, self-healing capabilities, and supports multiple APIs and data formats. Users can opt for hosted or self-hosted versions with detailed setup instructions available.

## Content (from Notion)

# data that speaks your language 🍯

superglue translates data from external systems into exactly the format you need. It’s an open source proxy that automatically extracts, maps and transforms data so developers don’t have to write and maintain complex integration code.

- 🔮 One-off LLM-powered translations: Generate deterministic, high-performance translation code.
- 🩹 Self-healing: Detect format changes and update translations automatically.
- 🚀 Fast deployment: Supports most APIs and data formats out of the box.
Loading

```plain text
flowchart LR
    subgraph Input[data sources]
        A1[APIs]
        A2[files]
        A3[legacy systems]
    end

    subgraph Process[data transformation]
        T1[superglue engine]
    end

    subgraph Output[destination]
        D1[your system]
    end

    Input --> Process
    Process --> Output

    %% Styling
    classDef sourceStyle fill:#f9f,stroke:#333,stroke-width:2px
    classDef processStyle fill:#bbf,stroke:#333,stroke-width:2px
    classDef outputStyle fill:#bfb,stroke:#333,stroke-width:2px

    class Input sourceStyle
    class Process processStyle
    class Output outputStyle

```

## quick start

### hosted version

1. 
1. 
```plain text
npm install @superglue/client
```

1. Configure your first api call:
```plain text
import { SuperglueClient } from "@superglue/client";

const superglue = new SuperglueClient({
  apiKey: "************"
});

const config = {
  urlHost: "https://futuramaapi.com",
  urlPath: "/graphql",
  instruction: "get all characters from the show",
  responseSchema: {
    type: "object",
    properties: {
      characters: {
        type: "array",
        items: {
          type: "object",
          properties: {
            name: { type: "string" },
            species: { type: "string", description: "lowercased" }
          }
        }
      }
    }
  }
};

const result = await superglue.call({endpoint: config});
console.log(JSON.stringify(result.data, null, 2));

/*
output:
{
  "characters": [
    {
      "name": "Phillip J. Fry",
      "species": "human"
    },
    ...
  ]
}
*/
```

### self-hosted version

Run your own instance of superglue using Docker:

1. Pull the Docker image:
```plain text
docker pull superglueai/superglue
```

1. Create a .env file with the following configuration:
```plain text
# Server Configuration

# Port to run the superglue server
GRAPHQL_PORT=3000

# Port to run the web dashboard
WEB_PORT=3001

# Endpoint the web interface will connect to
GRAPHQL_ENDPOINT=http://localhost:3000

# Authentication token for API access
AUTH_TOKEN=your-auth-token

# Datastore Configuration. Memory is faster but not persistent. Redis is slower but persistent.
DATASTORE_TYPE=redis or memory
# if redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_USERNAME=default
REDIS_PASSWORD=secret

# OpenAI Configuration
OPENAI_API_KEY=sk-...
# OpenAI model to use. We recommend gpt-4o-2024-11-20
OPENAI_MODEL=gpt-4o-2024-11-20
```

1. Start the server:
```plain text
docker run -d \
  --name superglue \
  --env-file .env \
  -p 3000:3000 \
  -p 3001:3001 \
  superglueai/superglue
```

1. Verify the installation:
```plain text
curl http://localhost:3000/health
> OK

# or open http://localhost:3000/?token=your-auth-token
```

1. Open the dashboard to create your first configuration:
```plain text
http://localhost:3001/
```

1. run your first call:
```plain text
npm install @superglue/client
```

```plain text
import { SuperglueClient } from "@superglue/client";

const superglue = new SuperglueClient({
  endpoint: "http://localhost:3000",
  apiKey: "your-auth-token"
});

// either via config object
const config = {
  urlHost: "https://futuramaapi.com",
  urlPath: "/graphql",
  instruction: "get all characters from the show",
};

const result = await superglue.call({endpoint: config});

// or via the api id if you have already created the endpoint
const result2 = await superglue.call({id: "futurama-api"});

console.log(JSON.stringify(result.data, null, 2));
```

## key features

- LLM-Powered Data Mapping: Automatically generate data transformations using large language models
- API Proxy: Intercept and transform API responses in real-time with minimal added latency
- File Processing: Handle various file formats (CSV, JSON, XML) with automatic decompression
- Schema Validation: Ensure data compliance with your specified schemas
- Flexible Authentication: Support for various auth methods including header auth, api keys, oauth, and more
- Smart Pagination: Handle different pagination styles automatically
- Caching & Retry Logic: Built-in caching and configurable retry strategies
## 📖 Documentation

For detailed documentation, visit docs.superglue.cloud.

## 🤝 contributing

We love contributions! Feel free to open issues for bugs or feature requests.

## license

superglue is GPL licensed. The superglue client SDKs are MIT licensed. See LICENSE for details.

## 🙋‍♂️ support

- 💬 Discord: Join our community
- 🐛 Issues: GitHub Issues

