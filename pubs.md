---
layout: page
permalink: /pubs/
title: Publications
---

<!-- ## Publications -->

{% assign thumbnail="left" %}
{% assign cur_year="0" %}

{% for pub in site.data.pubs %}
<!-- {% if pub.image %}
{% include image.html url=pub.image caption="" height="100px" align=thumbnail %}
{% endif %} -->
{% if cur_year != pub.year %}
{% assign cur_year = pub.year %}
## {{cur_year}}
{% endif %}
{% assign journal=pub.journal %}
{% assign js=site.data.abbr|where:"abbr",pub.journal %}
{% assign js_size=js|size%}
{% if js_size != 0 %}
{% assign journal=js[0].full %}
{% endif %}
* [**{{pub.title}}**]({{pub.file | prepend: site.fileurl | prepend: site.baseurl}})<br />
{% if pub.corespd %} {{pub.author|replace:'Hao Li','<u>Hao Li*</u>'}}<br /> {% endif %}
{% if not pub.corespd %} {{pub.author|replace:'Hao Li','<u>Hao Li</u>'}}<br /> {% endif %}
**{{journal}}** **{{pub.year}}**
<!-- {% if pub.note %} *({{pub.note}})* {% endif %}  -->
{% if pub.doi %}[[doi]({{pub.doi}})]{% endif %}
{% if pub.media %}{% for article in pub.media %}[[{{article.name}}]({{article.url}})]{% endfor %}{% endif %}

{% endfor %}
