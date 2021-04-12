---
layout: page
title: About
permalink: /
---
<!-- # About Me -->

{% include image.html url="images/avatar.jpg" caption="" width="150px" align="right" %}

**Hao Li (李昊)** is an associate professor at the [School of Computer Science and Technology](http://www.cs.xjtu.edu.cn), 
[Xi'an Jiaotong University](http://www.xjtu.edu.cn) in P.R. China. 
He received his Ph.D. degree from Department of Computer Science and Technology, Xi'an Jiaotong University in 2016. 
He is mainly interested in networked systems, including programmable networks, middleboxes and network verification.
He is a member of ANTS Lab.


**We Want You!**

I'm looking for self-motivated Master/Ph.D students to work with me at XJTU. 
Feel free to drop me an email with your CV.

Feel free to contact me too, if you are an undergradute and interested in internship opportunities in our group.

**Contact Info**

#234 Pengkang Building, Xingqing<br />
#6086 Hongli Building, iHabor<br />
[hao.li at xjtu.edu.cn]

## Selected Papers ([Full List](/pubs/))

<table style="font-size: 11pt;">
<tbody>
{% for pub in site.data.pubs %}
{% if pub.select == "true" %}
<tr> 
<td style="width:10em;"> <b>{{pub.journal}} {{pub.year}}</b> </td>
<td> <a href="{% if pub.internal %}{{pub.url | prepend: site.baseurl}}{% else %}{{pub.url}}{% endif %}">{{pub.title}}</a>  </td>
</tr>
<!-- {% if pub.doi %}[[doi]({{pub.doi}})]{% endif %} -->
<!-- {% if pub.media %}{% for article in pub.media %}[[{{article.name}}]({{article.url}})]{% endfor %}{% endif %} -->
{% endif %}
{% endfor %}
</tbody>
</table>

<!-- [Yavin]: https://en.wikipedia.org/wiki/Yavin -->
[hao.li at xjtu.edu.cn]: mailto:hao.li@xjtu.edu.cn
