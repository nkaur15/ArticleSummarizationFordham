# ArticleSummarizationFordham

Problem statement - Article summarization.
A substantial portion of RV's business is in publishers like Healthline and CNET. These publishers make money by displaying ads alongside the content. They do not use paywalls, so revenue is directly proportional the number of articles that users read. From this perspective, being a successful publisher is all about writing great content. This can be accomplished through many editorial strategies.

Red Ventures seeks to augment traditional editorial practices with data driven ones. Here are some questions that could inform an editorial strategy, which can be answered with data:

What are the top 10 articles this week about?
What are the topics our readers care most about?
What do we write most about?
Do we do more product reviews, news pieces, or opinion pieces?
What should we write about next?
How many words should be in a tech review?
Do readers prefer an active or passive voice?
How many articles do we have on auto-immune disorders? What about social media?
Now if every article published by a Red Ventures property had the same editor assign tags from a consistent set, write a summary, and log grammatical metadata, then we would be well on our way to answering many of these important questions. However, RV operates hundreds of sites, which publish articles from staff writers, freelancers, and experts in their field with sometimes very different editorial processes. If we wish to answer these questions at the portfolio level, we require tools to understand language in an automated and algorithmic way.

Summarizing content.
One common need, which allows us to make meaningful improvements in things like content recommendation, search engine optimization, and portfolio understanding, is the ability to summarize text.

Think about the movies you like to watch - what do they have in common? To answer this question you probably did not start replaying the movies in your head frame by frame, rather you probably thought about their summaries. In my case, they all happen to be murder mysteries set in dreary English estates. Should I watch "The ABC Murders" on Amazon Prime Video? Well, it's a murder mystery set in various dreary English locales, so yes, I probably will watch it.

The goal of this problem is to generate meaningful article summaries, which could be used as:

Data to create article recommendations.
Data to understand a body of articles.
Data to populate meta tags that search engines use to rank pages.
The Data
The data for this problem is a collection of 1,177 recent news articles from CNET, ZDNet, TVGuide, and GameSpot (4 technology focused properties in the CNET Media Group owned by Red Ventures) scraped on January 4, 2022.

Each article contains only an ID (from 0 to 1176), a source describing the site it was scraped from, and the article text. Since this text was scraped from the HTML, it may be messy and interspersed with links from outside of the article body.

This data is highly representative of the kind of data that practicing data scientists in industry commonly encounter.

The problem.
For each article, generate a summary of no more than 280 characters. Use these summaries to generate recommendations for each article to be interpretted as the article which the user should read next.

Work will be judged on both the intuitive quality of the summaries and recommendations.
