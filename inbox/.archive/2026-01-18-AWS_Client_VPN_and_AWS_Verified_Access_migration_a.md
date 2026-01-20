---
type: link
source: notion
url: https://aws.amazon.com/blogs/networking-and-content-delivery/aws-client-vpn-and-aws-verified-access-migration-and-interoperability-patterns/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-16T03:43:00.000Z
---

# AWS Client VPN and AWS Verified Access migration and interoperability patterns | Networking & Content Delivery

## AI Summary (from Notion)
- Secure Remote Connectivity: Emphasizes the need for secure, authenticated remote access to applications in modern workplaces.
- AWS Client VPN: A managed, OpenVPN-based solution for secure remote access introduced in 2018.
- AWS Verified Access: A newer approach launched in 2023 that follows Zero Trust principles, validating every application request without needing a client-based VPN.
- Integration Options: Discusses the potential for using both Client VPN and Verified Access together, providing pathways for integrating or migrating applications.
- Migration Scenarios:
- Client VPN Only: Initial setup using only Client VPN.
- Adding New Apps: Onboarding new applications directly with Verified Access while maintaining Client VPN for existing apps.
- Migrating Existing Apps: Transitioning existing applications to Verified Access while continuing to use Client VPN where necessary.
- Final Stage: Complete migration to Verified Access with the option to remove Client VPN or keep it as an alternative.
- Considerations:
- Verified Access currently supports only HTTP and HTTPS applications.
- Recommendations for using internal load balancers with Verified Access.
- Verified Access does not support IPv6 traffic yet.
- Conclusion: AWS Client VPN and Verified Access offer different methods for secure remote access, with a focus on migrating applications toward a VPN-less, Zero Trust model.
- Author's Background: Dave DeRicco is a Senior Networking Specialist at AWS, focusing on supporting enterprise customers with their global cloud networks.

## Content (from Notion)

In today’s workplace, your users need secure, authenticated remote connectivity to your applications. Until recently, many organizations took this requirement to mean “VPN connection.” AWS Client VPN, introduced in 2018, has provided AWS customers with a managed, OpenVPN-based VPN client solution for securing remote access to on-premises and AWS-hosted applications. AWS Verified Access, launched in 2023, takes a different approach to remote connectivity, based on Zero Trust guiding principles. Verified Access validates every application request before granting users access and, crucially, removes the need for a client-based VPN solution to access those applications.

With both solutions available, you might wonder: can you use Client VPN and Verified Access together? If so, how? How can you deploy new apps for Verified Access or migrate existing applications to Verified Access while still keeping Client VPN for the workloads that need it?

If you’re using Client VPN or a similar third-party VPN-based solution to provide secure access to your applications today, this post is for you. In this post, we look at the combined use of Client VPN and Verified Access and present a pathway for integrating new and existing applications into Verified Access in the future. These patterns can help you add the principles of Zero Trust security to your network.

## Overview of migration and interoperability patterns

We’ll look at four scenarios in this blog post, using a sample architecture with three applications to walk through the different patterns you can use:

1. Before Verified Access – Client VPN only
1. Adding new applications with Verified Access
1. Migrating existing applications to Verified Access
1. Verified Access only
## Before AWS Verified Access – AWS Client VPN only

When using Client VPN, your approach to accessing applications might look similar to the diagram in figure 1. In this example, we are hosting App A and App B behind their own private Application Load Balancers. Users must connect to AWS using Client VPN for secure access to these applications. We have isolated each application in its own Amazon Virtual Private Cloud (VPC), and we use to provide connectivity between the application VPCs, as well as with the Client VPN VPC. Users access App A and App B using fully qualified domain names (FQDNs), that is, app-A.example.com and app-B.example.com. In this scenario, we’re using the Amazon Route 53 DNS service to configure these records.

Figure 1: Accessing apps with Client VPN

Before going further, let’s review two configuration parameters on Client VPN that will affect how we work with Verified Access:

- Split-tunnel – We recommend enabling split-tunnel on the VPN endpoint if you plan on implementing Verified Access alongside your VPN. With split-tunnel enabled, only traffic destined to routes in the Client VPN endpoint route table is routed over the VPN tunnel. Otherwise, traffic to Verified Access applications is forced to traverse the VPN tunnel when the VPN is connected.
- DNS servers – If you don’t specify a custom DNS server in the Client VPN endpoint, your clients will use their locally configured DNS resolver to resolve domain names like App-A.example.com through a public hosted zone in Route 53. If you’re using a private hosted zone, for example.com instead, you must specify a custom DNS server such as a Route 53 Resolver inbound endpoint. When your clients perform a DNS query for App-A.example.com, they’ll receive a response from the private hosted zone.
For this and the following examples, we’ll assume you have configured your VPN with split-tunneling. Regardless, traffic to either app routes over the Client VPN through the Transit Gateway—these applications are not accessible without the VPN.

Now, let’s look at how we can deploy Verified Access for new applications.

## Adding new applications with AWS Verified Access

If you’re approaching Verified Access for the first time, you might decide to onboard new apps directly in Verified Access while maintaining your Client VPN solution for existing apps. Figure 2 shows our environment with a new application, App C, which we’ll configure for Verified Access.

Figure 2: Adding App C to the environment

To get started with Verified Access, you must create a trust provider to manage identity information for users and devices. In this example, we are using IAM Identity Center as a user trust provider, but you can configure any supported identity provider (IdP) or add an additional device trust provider. You’ll then create a Verified Access instance, attach the trust provider, and add a Verified Access group with any applicable policies to the instance. Optionally, you can integrate an AWS WAF access control list (ACL) with your Verified Access instance as well. For detailed step-by-step instructions for creating a new Verified Access application, check out the AWS Verified Access Preview — VPN-less Secure Network Access to Corporate Applications post on the AWS News blog channel. On the AWS Security blog, the A walk through AWS Verified Access policies post covers this topic as well.

The last step is to create a Verified Access endpoint, which represents an individual application. When creating the Verified Access endpoint, you must specify the DNS name for the application and a matching AWS Certificate Manager (ACM) certificate. In order for clients to resolve that DNS name correctly to the Verified Access application, create a Canonical Name Record (CNAME) record—we’ll use App-C.example.com—in your public hosted zone.

If you’ve configured your Client VPN with a custom DNS server IP and have a private hosted zone for your domain (such as example.com) associated with the Client VPN VPC, there’s one last step to remember. You must create a matching CNAME record in your private hosted zone to ensure your clients can resolve the App C FQDN correctly while connected to the VPN. To explain why, let’s zoom in on the different DNS flows that are possible when using Verified Access alongside Client VPN. This is shown in figure 3: DNS resolution on VPN with custom DNS.

Figure 3: DNS resolution when connected to Client VPN with custom DNS

Here’s what happens:

1. The client performs a DNS query for App-C.example.com. Because we have our inbound endpoint set as a custom DNS server in the Client VPN configuration, the endpoint will act as our resolver.
1. The inbound endpoint sends the query to Route 53 Resolver, which uses the private hosted zone for example.com that is associated with the Client VPN VPC to resolve the query. Resolver returns the CNAME for App C’s Verified Access endpoint to the inbound endpoint, which returns that value to the client.
1. The client initiates a connection to App C’s Verified Access endpoint over the internet.
What if you’re connected to Client VPN without custom DNS configured? As figure 4 shows, the behavior is just the same as if you were using Verified Access to access App C.

Figure 4: DNS resolution when connected to VPN with no custom DNS or off VPN

If no DNS server is set on the Client VPN or when the client is off VPN:

1. As before, the client performs a DNS query for App-C.example.com. In this case, no custom DNS server is set on the VPN, so the client will use its local DNS resolver to perform a recursive lookup against public name servers. Similarly, when the client is off the VPN, it will also use the local resolver.
1. The local resolver queries the public hosted zone for App-C.example.com. Route 53 will respond with the CNAME value from the public hosted zone for example.com, which the local resolver returns to the client.
1. The client initiates a connection to App C’s Verified Access endpoint over the internet.
Assuming you’ve enabled split-tunnel on your Client VPN as recommended, the resulting connectivity will look like figure 5: App C with Verified Access. Users continue to connect to App A and App B through the Client VPN connection. The FQDN for App C resolves to the Verified Access endpoint, and App C can be accessed with or without the VPN.

Figure 5: App C with Verified Access

## Migrating existing applications to AWS Verified Access

As you become more experienced with Verified Access and Zero Trust principles, you can migrate your existing applications away from a VPN-based approach. Let’s continue with the example architecture by enabling App A for Verified Access, as shown in figure 6.

Figure 6: Enabling App A for Verified Access

If you are planning on using the same trust providers for all of your applications, you can continue to use the existing Verified Access instance created for App C. Similarly, applications with the same security requirements and a shared common policy can use the same Verified Access group. Otherwise, you can create separate Verified Access instances or Verified Access groups to meet your requirements.

Create a new Verified Access endpoint and specify the DNS name and appropriate ACM certificate for the application (App-A.example.com). Once the endpoint is active, create the CNAME record in your public hosted zone.

As before, if you’re resolving private hosted zones through a custom DNS server, you’ll must also update the record for App-A.example.com in the private hosted zone associated with the Client VPN endpoint VPC. If you’re using a non-alias record, make sure to lower the time to live (TTL) before making any changes – Route 53 will manage alias record TTLs. Figure 7 shows the new and updated records for App A.

Figure 7: New and updated DNS records for App A

Once your DNS updates, the migration is complete. Figure 8: Application A migration complete shows the results, with App A now only accessible through Verified Access. Queries for App-A.example.com will now resolve to the CNAME record pointing to the Verified Access endpoint, while App B is still only accessible over the VPN.

Figure 8: Application A migration complete

If you have other applications that do not use HTTP/HTTPS, or your security requirements mandate a VPN for specific use cases, you may choose to finish your adoption of Verified Access here. You can keep using Client VPN for applications that require it and use Verified Access where desired. Otherwise, you can continue to migrate your remaining applications to Verified Access.

## AWS Verified Access only

The final potential stage for your migration is using Verified Access with all of your applications, following the approach discussed previously. Once you migrate all applications to Verified Access, you can decide whether to remove Client VPN altogether or keep it as an alternate connectivity method. Figure 9: All applications migrated to Verified Access shows our environment when only using Verified Access.

Figure 9: All applications migrated to Verified Access

Note that we’ve entirely removed the Client VPN VPC and the inbound resolver endpoints. All DNS resolution from the client to our Verified Access applications is handled by the public hosted zone, with no need to worry about managing both public and private hosted zones.

## Considerations

- Verified Access supports HTTP and HTTPS applications today. For applications that require support for protocols like Secure Shell (SSH), you can continue to use Client VPN in tandem with Verified Access.
- Load balancer endpoints only support internal load balancers (Application Load Balancer or Network Load Balancer). If your applications are using an external or public-facing load balancer, you must create a new internal load balancer for use with Verified Access.
- Verified Access does not support IPv6 traffic today; however, your load balancers can continue to operate in dual-stack mode and route traffic to both dual-stack and IPv6-only targets. If you would like to learn more, the Dual-stack IPv6 architectures for AWS and hybrid networks post on the Networking and Content Delivery Blog channel will be helpful.
## Conclusion

AWS Client VPN and AWS Verified Access provide you with two options for enabling secure remote access to your applications, with Verified Access based on VPN-less Zero Trust principles. This post discussed patterns for using Client VPN and Verified Access together, as well as approaches to migrating your applications to Verified Access from Client VPN.

Check out the AWS Verified Access documentation to start onboarding your applications today. For more information about AWS Client VPN, take a look at the AWS Client VPN documentation. And if you’re a hands-on kind of person, dive in to the AWS Verified Access Workshop and the AWS Client VPN Workshop. Where will you start first?

## About the author

### Dave DeRicco

Dave DeRicco is a Senior Networking Specialist Technical Account Manager (STAM) within Enterprise Support at Amazon Web Services. By day Dave helps enterprise customers architect, operate, and manage their global cloud networks. Dave is also an open source contributor and particularly interested in network automation with infrastructure as code (IaC). When not chasing after his kids or making a mess in the kitchen, Dave is most likely exploring a new city or a trail in the woods with a coffee in hand.


