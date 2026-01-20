---
type: link
source: notion
url: https://knowingmachines.org/models-all-the-way#section2
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-31T02:44:00.000Z
---

# Models All The Way Down

## AI Summary (from Notion)
- LAION-5B Overview: LAION-5B is a large dataset constructed from web data, primarily sourced from Common Crawl, containing over 5 billion image-text pairs.

- Data Sources: Key contributors to LAION-5B include Pinterest, Shopify, and SlidePlayer, with a significant number of images having ALT tags that align with commercial interests rather than accurate descriptions.

- Algorithmic Curation: The dataset is heavily influenced by algorithms like CLIP, which score image-text similarity. The choice of thresholds for inclusion can drastically affect the dataset's composition.

- Bias and Representation: English content is prioritized in LAION-5B, reflecting biases in the web data. The dataset lacks adequate representation for many languages and cultures, raising concerns about the worldview encoded in AI models trained on it.

- Circularity of Training Sets: LAION-5B's construction involves multiple layers of models and datasets, leading to compounded biases and blind spots in AI training.

- Aesthetic Bias: LAION has created specialized subsets like LAION-Aesthetics, which cater to specific visual quality preferences based on narrow demographic inputs, affecting generative AI outputs.

- Ethical Considerations: Questions arise around ownership and safety related to the images and text in the dataset, with LAION recognizing the imperfection of their watermark and NSFW content metrics.

- Transparency and Accountability: LAION publishes its datasets as open-source, which is vital for understanding biases in AI systems and advocating for responsible use and transparency in dataset construction.

- Recent Developments: Following concerns raised about CSAM, LAION-5B is currently unavailable for download, with developers working on remediation. A new dataset called CommonPool has been released, containing 12.8 billion curated image pairs.

## Content (from Notion)

Part 2: Seeing Like an Algorithm

LAION-5B was itself built from an even larger dataset, which comes from another non profit organization: Common Crawl.

Common Crawl is a corpus of web data that comes from a monthly crawl of the web. It contains data for more than 3 billion websites.

Some of these websites in particular are very well-represented in LAION-5B.

There are nearly 155 million images pairs (images + captions) from Pinterest - about one in every forty pairs.

2,4% of LAION-5B - 140 million image pairs - comes from Shopify.

72 million pairs are from SlidePlayer, a platform for storing and sharing PowerPoint presentations.

These particular domains are well represented in LAION-5B in part because they host a lot of images.

On top of that, content from these three sites is served up in a way that makes it particularly appealing to LAION’s methods of statistical curation.

To make LAION-5B, developers processed Common Crawl looking for HTML IMG tags which have an ALT attribute.

The intended purpose of the ALT attribute is to improve accessibility, in particular for vision-impaired users who use screen readers.

Under 40% of the images across the web have ALT tags. But for some sites this is much higher.

SlidePlayer, for example, seems to add ALT tags automatically, populating them with text from the PowerPoint slides it ingests.

Pinterest generates the captions on its pages from the ALT tags, so users learned to write them before they ‘pinned’ their images.

Shopify users often have their eyes on high Google PageRank scores, and write ALT tag descriptions with SEO (Search Engine Optimization) in mind.

All of this means that ALT tags are not so much descriptions of image contents as they are artifacts of the web’s workings and of creators’ retail ambitions.

The content of an ALT tag should describe what is in the image.

## IMAGE

Garden center worker selling potted flower

## ALT TEXT

Garden center worker selling potted flower

However, ALT tags most often describe what the site's owners want algorithms to see, not what they want humans to see.

## IMAGE

Heart Shaped Sunnies - Chynna Dolls Swimwear

## ALT TEXT

Heart Shaped Sunnies - Chynna Dolls Swimwear

Here we find an important truth about LAION-5B:

It contains less about how humans see the world than it does about how search engines see the world. It is a dataset that is powerfully shaped by commercial logics.

A key part of LAION-5B's construction was to try to select images and text captions from Common Crawl where the text of the ALT attribute most closely matched the contents of the image.

To do this, LAION developers used a model called CLIP (Contrastive Language–Image Pre-training), a neural network developed by researchers at Open AI.

The developers used CLIP to get a score for how well a string of text matches to an image: a metric for similarity between the image and its ALT tag.

LAION-5B's authors used this score to determine which images and text captions from Common Crawl would end up in their dataset.

To arrive at a minimun acceptable score, LAION-5B trained a model with samples from Common Crawl against popular benchmark datasets, such as ImageNet-1K.

They determined that image/text pairs with a similarity scores above a threshold of 0.26 - 0.28 (depending on the language of the caption) would be included in LAION.

This one thin sliver of a threshold is the thing that, more than anything else, defines which images LAION-5B contains.

CLIP, like most neural networks, is hard to reverse engineer. OpenAI is not forthcoming about the data that CLIP was trained on. The image pairs in LAION - and their scores - give us a glimpse into some of its workings.

By looking at images at the extreme edges of LAION-5B’s similarity thresholds, we can get a sense of how CLIP perceives images, and how the use of this score might influence what LAION includes and excludes.

High similarity scores tend to be given to pairs where there is text in the image that matches the ALT tag exactly.

The CLIP scores that the LAION team generated seem to have upward bounds in the 0.5 range; there are only 22,645 images in the entire 5B set that score higher than 0.5.

Here is a set of image/text pairs with similarity scores > 0.46

These are mostly pairs where the images contain text, and where the ALT tags match that text.

Looking across LAION-5B, it's clear that these CLIP scores are very unequally distributed.

Very often the scores are near LAION's chosen threshold.

A full 16% of the total images across all subsets have scores within 0.1 of the lower bounds.

This means if the LAION developers had chosen to nudge the CLIP similarity threshold up by just 0.01, they would have removed 937,489,831 pairs from the set.

The tiniest of shifts in LAION's thresholds could have excluded or included hundreds of millions of images.

What the images contain plays no role at all in deciding what stays and what goes.

This is what curation by statistics looks like: tiny tweaks to code can have profound effects on the content of training sets, and on the models that use them to shape their computational worldview.

There are two important things we can learn here.

First, that algorithmic curation commonly depends on numeric thresholds which are very often poorly understood.

For decades datasets were constructed by human intervention. This generally yielded datasets that are of high quality but too small to make today's LLM’s yield meaningful results.

LAION set out to build a dataset for these newer, hungrier models. They built a dataset that is purely constructed by machine processes, by running models and tweaking thresholds: LAION-5B is made by measure.

But what is getting measured? The quality of data? The capacities of CLIP? The success of a model against a benchmark? The benchmark itself?

Second, that there is a circularity inherent to the authoring of AI training sets.

Because they need to be so large, their construction necessarily involves the use of other models, which themselves were trained on algorithmically curated training sets.

Consider LAION-5B’s similarity score. It is the result of a model (CLIP) trained on a dataset (which OpenAI does not disclose).

To arrive at a threshold, LAION made another model, trained on a fraction of their own dataset, and compared it to benchmarks (e.g. ImageNet-1K).

The gold standard for this benchmark was set in 2020 by a third model, a widely-used neural network called ResNet50.

There are models on top of models, and trainings sets on top of training sets.

Omissions and biases and blind spots from these stacked-up models and training sets shape all of the resulting new models and new training sets.

It's only by looking at datasets that we can get a better sense of how AI models work, and the gaps, errors, and biases that can emerge.

Part 3: LAION-5B's Great Divide

It's convenient to refer to LAION-5B in the singular: as one gigantic training set.

In reality, most researchers who train models with LAION-5B use a subset of the data, constructed with a specific purpose or task in mind.

Indeed, there is no way to directly download all of LAION-5B; instead you need to choose one of three language subsets.

## LAION-2B EN

2.3 billion image-text pairs where the text was algorithmically identified as English.

## LAION-2B MULTI

2.26 billion image-text pairs where the text was algorithmically identified as a non-English language.

## LAION-1B NOLANG

1.27 billion image-text pairs where the language couldn't be detected by the algorithm, or the confidence level was too low.

To make these subsets, LAION developers again relied on a machine learning model developed by Google called CLD3 (Compact Language Detector 3) to classify the language of the ALT attribute into one of 107 language classes.

Beside English, Russian is the most common language that can be found in the set. Russian is followed by French and then German.

For each of the 255 million Russian speakers on the planet, there is one image in the dataset labeled as Russian.

For every 2 French speakers there is one image caption labeled as French.

For every 35 of the 71.6 million Swahili speakers on Earth, there is one image caption in LAION-5B labeled as Swahili.

On the other hand, for every English speaker on the planet there are 1.6 captions labeled as English.

For every Dutch speaker there are 3 captions in LAION-5B labeled as Dutch.

For every Icelandic speaker there are 7 image captions labeled as Icelandic.

These statistics tell us less about the composition of the originating dataset - Common Crawl - than they do about the shortcomings of the language detection model the LAION-5B developers chose to use.

The language distribution differs significantly between Common Crawl and LAION-5B.

That is, the quantity of pages in a language in Common Crawl may not match the number of images in LAION-5B for the same language.

To give a stark example, there are 34,270,773 text captions in LAION-5B which CLD3 has classified as Luxembourgian: a language that only 300,000 people speak. This is 1 caption for every 114 images.

Meanwhile there are only around 53,500 pages classified as Luxembourgian in the Common Crawl: 1 for every 58,000 pages.

Looking at a set of supposedly Luxembourgian image pairs, we can quickly see that the ALT text is mostly English or in a different language altogether.

Exactly why CLD3 fails toward Luxembourgish is a question for another investigation (and another training set).

It does, however, offer a particularly clear example of how LAION’s ‘hands-off’ processes fail.

Despite the fact that many English captions seem to have been mis-classified as other languages, it's obvious that LAION-5B as a whole prioritizes English content.

This prioritization can also be observed in the fundament that LAION-5B is built upon – Common Crawl, where about 45% of websites have primarily English language content.

This split tells us something specific about the worldview that LAION-5B contains; a perspective that is carried into AI models that are trained on it.

For models trained on LAION-5B, English (and English-speaking culture) is valued more than the other 107 languages combined.

The creators of LAION-5B are aware of the representative shortcomings of Common Crawl, when it comes to language and cultural representation.

But they deem the situation workable. Their whole endeavour, after all, is a research project, not to be used to create 'ready-to-go industrial projects'.

Yet the LAION team has created other subsets of their really big dataset, built to satisfy the very particular needs of consumer-facing generative AIs.

Part 4: Made to Fit

Besides the language subsets, LAION has released several other datasets based on LAION-5B targeted toward specific purposes.

Perhaps the most interesting of these is LAION-Aesthetics, a subset intended to include images that have "high visual quality".

Ask Midjourney or Stable Diffusion to generate an image for you, and you’ll get a result that has been fine-tuned on this subset of LAION.

The model used to build this subset was trained on three sources: 15,000 images of logos, as well as two different batches of images that were rated by humans to be visually appealing.

One batch of images came from a training set called Simulacra Aesthetic Captions (SAC). This set contains synthetic images, produced by Generative AIs including CompVis latent GLIDE and Stable Diffusion.

These synthetic images – 238,000 of them – were rated by users of the Discord communities for GLIDE and Stable Diffusion.

Users were asked to rate images on a scale of 1 to 10.

These images are a sample of the 176,000 top scoring ones in the set.

The creators of SAC are transparent about the shortcomings of the set, specifically the fact that the scores were submitted by users who were both WEIRD (Western, Educated, Industrialized, Rich, and Democratic) and developers of AI art, a demographic they describe as leaning toward "nerdy" and "esoteric."

Furthermore, they admit that most of the ratings in the dataset were submitted by a "handful of users," whose "aesthetic preferences dominate the dataset."

Another of the aesthetic training sets uses images scored on the website dpchallenge.com, which is described as a "digital photography challenge".

250,000 images were scraped from the website, along with user-contributed ratings, for the Aesthetic Visual Analysis (AVA) dataset.

Here is a sample of the highest rating images from the set.

dpchallenge.com posts a leaderboard of image reviewers.

The top 50 reviewers, responsible for more than 7.5 million total reviews, appear to fall neatly in the WEIRD demographic.

Of the 41 users who share location info, 95% are in the US, Canada, or Europe.

They are, mostly, middle-aged photography enthusiasts from small American cities.

Using the SAC set, LAION-Logos and AVA images, LAION developers trained a model called LAION-Aesthetics_Predictor V2.

This model produces an aesthetic score based on the output from the CLIP model's analysis of an image.

They used this model to score the English language set (2.3 billion images) and released a series of subsets with different score thresholds.

The smallest of these subsets, with 600 million images scoring 5 or higher, was used by Midjourney to fine-tune the results of their model, with the goal to produce output that would be more appealing to the users of their tool.

Here we find another truth about generative AI:

The concepts of what is and isn't visually appealing can be influenced in outsized ways by the tastes of a very small group of individuals, and the processes that are chosen by dataset creators to curate the datasets.

In the case of Midjourney, by a handful of esoteric nerds, and by a 65-year old mechanical engineer living in Southeastern Wisconsin.

Part 5: Big is the new small.

Over the last two years, generative AI models have forced people to ask hard questions about ownership and about safety.

At the root of these conversations are training sets like LAION-5B, whose contents cross all manner of boundaries (both ethical and legal).

The LAION-5B training set does address both ownership and safety, albeit in a typically statistical fashion.

For image ownership, the LAION-5B set offers a score indicating the probability that the image is watermarked, and a flag for NSFW content.

Both of these metrics were produced by models created by LAION.

The researchers admit that these models are "not perfect."

Again, the caveat: that the metrics should not be used to create “production-ready” subsets.

This is a convenient way to avoid responsibility, and leans heavily on a core philosophy of software-based research: that if you make the problems visible, someone down the line will step up and fix them.

In their paper, the LAION devs "advocate using these tags responsibly," to not rely on them for making "truly safe" versions of their dataset.

Beyond that, no advice is given about what responsible use might look like.

Responsible use might start with a more careful look at how these scores connect to the content of the pages from which the images and text captions were collected.

There is one thing in particular that LAION get right: they publish their datasets as open-source.

In the field of AI they are alone in doing so. It is what allowed us to dissect LAION-5B in the first place.

Openness in the AI field matters, not just for model biases, but for the structural biases in the ecosystem. An ongoing problem is that curation by statistics amplifies many of those structural biases.

Driven by investments going into the trillions, datasets and AI models, which are too complex or large to be truly understood, are being deployed with a break-neck speed.

As artists, academics, practitioners, or as journalists, dataset investigation is one of the few tools we have available to gain insight and understanding into the most complex systems ever conceived by humans.

This is why advocating for dataset transparency is so important if AI systems are ever going to be accountable for their impacts in the world.

LAION-5B has, since the CSAM findings in December, been unavailable for download.

The developers say they are working on remediating it.

In the meantime, they've released a new dataset of images and textcalled CommonPool, which contains 12.8 billion image pairs.

12.8 billion images pairs, culled from Common Crawl.

12.8 billion images pairs, scored by CLIP.

12.8 billion images pairs, curated by statistics.

This piece was created by Knowing Machines, a research project tracing the histories, practices, and politics of how machine learning systems are trained to interpret the world.

knowingmachines.org

Special thanks to Kate Crawford and Michael Weinberg.


