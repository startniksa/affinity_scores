# affinity_scores

## Given

A csv file with the information on content consumption by a subset of our users in the UK.

Every row represents a separate event of the user engagement with the content. 

There are
three types of engagement in the file, identified by the value in source_system column:

● PX - page views on the web portal

● Activecampaign - interaction with the content within newsletter (i.e. clicking on a link)

● Catalogue - download of the pdf catalogue of the product category related to a
specific topic

Content items can be identified by the content_id column (can be numeric ID or an URL).

Users are identified by scv_id column. Topics for each content item are specified in the
topic column (several topics in a single row means that a specific content item was
categorised with multiple topics at the same time). Date column represents the date of
engagement

## Task

The goal of the task is to understand which topics our users are mostly interested in, taking
into account their past content consumption, in order to be able to segment users
accordingly for further targeted communication.

Implement a Python routine to calculate topic affinity score (i.e. interest score) for
each user/topic combination based on 3 types of engagement as per above. More
engagement with the topic obviously means more interest in it. Generate a csv file
with the result.
Take the following into account:

● Affinity score should be in the range between 0 and 10, where 0 is no affinity
with the topic, and 10 is the highest affinity with the topic

● All three types of engagement should be weighted equally in the calculation

● We are only interested in engagements happened during 2023