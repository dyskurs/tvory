---
layout: default
---


# Катэгорыі
<div class="posts">
  {% for p in site.pages %}
  {% if p.layout == "tag" %}
    <li><a href="{{p.url}}">{{p.title}}</a></li>
    {% endif %}
  {% endfor %}
</div>