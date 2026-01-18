---
type: link
source: notion
url: https://nh3.readthedocs.io/en/latest/
notion_type: Software Repo
tags: ['Running']
created: 2025-08-24T12:51:00.000Z
---

# nh3 documentation

## Overview (from Notion)
- The documentation focuses on sanitizing HTML, crucial for web development, especially in ensuring safety and security against XSS attacks.
- Understanding API references and Python bindings can improve your efficiency as a software engineer, allowing you to integrate and utilize libraries more effectively.
- The emphasis on customizable sanitization settings reflects the need for tailored solutions in software projects, particularly when dealing with user-generated content.
- As a founder, utilizing such tools can enhance product stability and user trust, which is vital for startup success in a competitive market like NYC.
- Consider the balance between security and user experience; overly aggressive sanitization can frustrate developers and users alike, leading to a need for thoughtful implementation.
- Explore alternative views on sanitization—some might argue that strict filtering can hinder functionality, while others emphasize the importance of security above all.

## AI Summary (from Notion)
This documentation provides an overview of the nh3 library, which offers Python bindings to the ammonia HTML sanitization library. It details the usage of the clean() function for sanitizing HTML fragments, including options for allowed tags, attributes, and handling of comments. Key features include customizable sanitization settings, support for various HTML attributes, and security measures like rel attributes to prevent XSS attacks.

## Content (from Notion)

   
• API reference  

- • API reference
Python bindings to the ammonia HTML sanitization library.

## Usage

Use clean() to sanitize HTML fragments:

It has many options to customize the sanitization, as documented below. For example, to only allow <b> tags:

## API reference

Python bindings to the ammonia HTML sanitization library ( https://github.com/rust-ammonia/ammonia ).

 , , , , , , , , , , ,  Create a reusable sanitizer according to the given options.    
• tags (set[str], optional) – Sets the tags that are allowed. 
• clean_content_tags (set[str], optional) – Sets the tags whose contents will be completely removed from the output. 
• attributes ( , optional) – Sets the HTML attributes that are allowed on specific tags, * key means the attributes are allowed on any tag. 
• attribute_filter ( , optional) – Allows rewriting of all attributes using a callback. The callback takes name of the element, attribute and its value. Returns None to remove the attribute, or a value to use. 
• strip_comments (bool) – Configures the handling of HTML comments, defaults to True. 
• link_rel (str) – 
Configures a rel attribute that will be added on links, defaults to  . To turn on rel-insertion, pass a space-separated list. If rel is in the generic or tag attributes, this must be set to None. Common rel values to include:  
    ◦ noopener: This prevents a particular type of XSS attack, and should usually be turned on for untrusted HTML. 
    ◦ noreferrer: This prevents the browser from sending the source URL to the website that is linked to. 
    ◦ nofollow: This prevents search engines from using this link for ranking, which disincentivizes spammers.   
• generic_attribute_prefixes (set[str], optional) – Sets the prefix of attributes that are allowed on any tag. 
• tag_attribute_values ( , optional) – Sets the values of HTML attributes that are allowed on specific tags. The value is structured as a map from tag names to a map from attribute names to a set of attribute values. If a tag is not itself whitelisted, adding entries to this map will do nothing. 
• set_tag_attribute_values ( , optional) – Sets the values of HTML attributes that are to be set on specific tags. The value is structured as a map from tag names to a map from attribute names to an attribute value. If a tag is not itself whitelisted, adding entries to this map will do nothing. 
• url_schemes (set[str], optional) – Sets the URL schemes permitted on href and src attributes. 
• allowed_classes ( , optional) – Sets the CSS classes that are allowed on specific tags. The values is structured as a map from tag names to a set of class names. The class attribute itself should not be whitelisted if this parameter is used. 
• filter_style_properties (set[str], optional) – Only allows the specified properties in style attributes. Irrelevant if style is not an allowed attribute. Note that if style filtering is enabled style properties will be normalised e.g. invalid declarations and @rules will be removed, with only syntactically valid declarations kept.   

- •
- •
- •
- •
- •
- •  
- noopener: This prevents a particular type of XSS attack, and should usually be turned on for untrusted HTML.
- noreferrer: This prevents the browser from sending the source URL to the website that is linked to.
- nofollow: This prevents search engines from using this link for ranking, which disincentivizes spammers.
- •
- •
- •
- •
- •
- •
 html, , , , , , , , , , , ,  Sanitize an HTML fragment according to the given options. See Cleaner() for detailed sanitizer options.  
For example:    
Example of maintaining the rel attribute:

Turn an arbitrary string into unformatted HTML. 
Roughly equivalent to Python’s html.escape() or PHP’s htmlspecialchars and htmlentities. Escaping is as strict as possible, encoding every character that has special meaning to the HTML parser.  
For example:

 html Determine if a given string contains HTML. 
This function parses the full string and checks for any HTML syntax. 
Note: This function will return True for strings that contain invalid HTML syntax like <g> and even Vec::<u8>::new().  
For example:

The default set of tags allowed by clean(). Useful for customizing the default to add or remove some tags:

The default mapping of tags to allowed attributes for clean(). Useful for customizing the default to add or remove some attributes:

The default set of URL schemes permitted on href and src attributes. Useful for customizing the default to add or remove some URL schemes: 



```plain text
  '<a rel="noopener noreferrer">Call</a> or <a href="mailto:contact@me" rel="noopener noreferrer">email</a> me.'

```


