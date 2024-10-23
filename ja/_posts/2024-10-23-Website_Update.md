---
# multilingual page pair id, this must pair with translations of this page. (This name must be unique)
lng_pair: id_webupdate
title: サイト大更新

# post specific
# if not specified, .name will be used from _data/owner/[language].yml
# author: Mr. Green's Workshop

# multiple category is not supported
category: misc

# multiple tag entries are possible
tags: [jekyll, website]

# thumbnail image for post
img: ":home-heading-2024-10-22.jpg"

# disable comments on this page
#comments_disable: true

# publish date
date: 2024-10-23 00:13:36 +0800

# seo
# if not specified, date will be used.
#meta_modify_date: 2022-02-10 08:11:06 +0900

# check the meta_common_description in _data/owner/[language].yml
#meta_description: ""

# optional
# please use the "image_viewer_on" below to enable image viewer for individual pages or posts (_posts/ or [language]/_posts folders).
# image viewer can be enabled or disabled for all posts using the "image_viewer_posts: true" setting in _data/conf/main.yml.
image_viewer_on: true

# please use the "image_lazy_loader_on" below to enable image lazy loader for individual pages or posts (_posts/ or [language]/_posts folders).
# image lazy loader can be enabled or disabled for all posts using the "image_lazy_loader_posts: true" setting in _data/conf/main.yml.
image_lazy_loader_on: true

# exclude from on site search
#on_site_search_exclude: true

# exclude from search engines
#search_engine_exclude: true

# to disable this page, simply set published: false or delete this file
#published: false
---

<!-- outline-start -->

このウェブサイトをついにアップデートしました！

<!-- outline-end -->

> 日本訳がありませんでごめんなさい。訳は難しくて長い過程ですので、ほとんどのブログは英語だけで書いています。ブログを読みたい場合は、翻訳ツールを使用してください。

This is the first major change to this website ever since it was first rushed and created back in October 29, 2023.

Very special thanks to [Mr. Green's Workshop](https://github.com/MrGreensWorkshop/MrGreen-JekyllTheme){:target="_blank"},
I've adopted his template, made some personal modifications, and transferred content to it.
Everything looks so pretty now and suddenly there are so many features such as an entire blogs system, site search, and more!
I've also made use of the multi-language support and added Japanese translation for the whole site,
I did my best to translate as accurately as I can and I hope I'm understandable! I first constructed
words and sentences by myself and with the use of a dictionary, and asked ChatGPT and other translation services
for corrections and explanations.

### Markdown Guide

Anyway, this also contains an example page to display markdown related styles for Mr. Green Jekyll Theme.
(and also contains documentation for liquid properties in the source code)

### Headings (this one is centered)
{:data-align="center"}

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

***

### Paragraphs

#### Paragraph

**William Shakespeare**, Let me not to the marriage of true minds
Admit impediments. Love is not love
Which alters when it alteration finds,
Or bends with the remover to remove.
O no, it is an ever-fixed mark
That looks on tempests and is never shaken;
It is the star to every wand'ring barque,
Whose worth's unknown, although his height be taken.
Love's not Time's fool, though rosy lips and cheeks
Within his bending sickle's compass come;
Love alters not with his brief hours and weeks,
But bears it out even to the edge of doom.
If this be error and upon me proved,
I never writ, nor no man ever loved.

#### Texts

Quoted text `Hello world`

Bold text **Hello world**

Italic text _Hello world_

kbd text <kbd>Hello world</kbd>

#### Blockquote

> **William Shakespeare**, Let me not to the marriage of true minds
> Admit impediments. Love is not love
> Which alters when it alteration finds,
> Or bends with the remover to remove.
> O no, it is an ever-fixed mark
> That looks on tempests and is never shaken;
> It is the star to every wand'ring barque,
> Whose worth's unknown, although his height be taken.
> Love's not Time's fool, though rosy lips and cheeks
> Within his bending sickle's compass come;
> Love alters not with his brief hours and weeks,
> But bears it out even to the edge of doom.
> If this be error and upon me proved,
> I never writ, nor no man ever loved.

### Link

This is [Mr. Green Jekyll Theme](https://github.com/MrGreensWorkshop/MrGreen-JekyllTheme), a simple theme built for [Jekyll](https://jekyllrb.com/).

\* Hello world! This is **[{{ site.data.owner[site.data.conf.main.default_lng].brand }}]({{ site.url }})**

### Picture

![such a lovely place](:projects-heading-2024-10-23.jpg)

[Art by Krab]({{ site.data.conf.others.projects.image_credit_url }})

### Picture (centered)

![such a lovely place](:home-heading-2024-10-22.jpg){:data-align="center"}

[Art by kieed](https://www.pixiv.net/en/artworks/118314218){:target="\_blank"}

### Lists

- Apple
- Banana
- Orange

1. Fruits
   1. Apples
      - Granny Smith
      - Mutsu
   1. Bananas
      - Cavendish
      - Red
1. Vegetables

***

### Tables

#### Small Table (centered)

| Fruits(not aligned) | Alignment (centered) | num (right align) |
| ------------------- | :------------------: | ----------------: |
| Apple               |       centered       |              9999 |
| Banana              |  centered long text  |               999 |
| Orange              |       centered       |                99 |
| Lemon               |       centered       |                 9 |
{:data-align="center"}

#### Wide Table (centered)

scroll enabled when page is narrow

| Fruits | num (left align) | num (right align) | num  | num  | num  |
| ------ | :--------------- | ----------------: | ---- | ---- | ---- |
| Apple  | 1111             |              1111 | 2222 | 3333 | 4444 |
| Banana | 111              |               111 | 222  | 333  | 444  |
| Orange | 11               |                11 | 22   | 33   | 44   |
| Lemon  | 1                |                 1 | 2    | 3    | 4    |
{:data-align="center"}

#### Wider Table

scroll enabled when page is narrow

| Fruits | num (left align) | num (right align) | num  | num  | num  | num  | num  | num  |
| ------ | :--------------- | ----------------: | ---- | ---- | ---- | ---- | ---- | ---- |
| Apple  | 1111             |              1111 | 2222 | 3333 | 4444 | 5555 | 6666 | 7777 |
| Banana | 111              |               111 | 222  | 333  | 444  | 555  | 666  | 777  |
| Orange | 11               |                11 | 22   | 33   | 44   | 55   | 66   | 77   |
| Lemon  | 1                |                 1 | 2    | 3    | 4    | 5    | 6    | 7    |

### Code

#### Highlight

{% highlight python %}

@command(aliases=["audr"])
async def audrna(ctx: Context):
    """ audrNa """
    URL: str = "https://audrna.github.io"

    view = discord.ui.View()
    button = discord.ui.Button(label="Go", url=URL, style=discord.ButtonStyle.link)
    view.add_item(button)
    await ctx.reply(f"# [audrNa](<{URL}>)", view=view)
{% endhighlight %}

#### Quote

```python
>>> f  = 3
>>> ck = 23
>>> f*ck
69
>>> ▮
```
