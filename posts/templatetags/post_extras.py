import re
from django import template
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_post(post):
    images = list(post.images.all())
    out = []
    for block in re.split(r"\n\s*\n", post.content.strip()):
        match = re.fullmatch(r"\[\[image (\d+)\]\]", block.strip())
        if match:
            n = int(match.group(1)) - 1
            if 0 <= n < len(images):
                img = images[n]
                cap = format_html("<figcaption>{}</figcaption>", img.caption) if img.caption else ""
                out.append(format_html(
                    '<figure class="image"><img src="{}" alt="{}">{}</figure>',
                    img.image.url, img.caption or post.title, cap,
                ))
        else:
            out.append(format_html("<p>{}</p>", mark_safe(escape(block).replace("\n", "<br>"))))
    return mark_safe("".join(out))