---
# Metadata
title: &title New Codestar Marp theme
author: Hamza Haiken
header: *title  # Header set to the same value as the title, can be changed if needed
footer: Example slides

# Appearance
# Uncomment for dark mode
# class: invert
transition: wipe

# Don't change
marp: true
theme: codestar
paginate: true
math: mathjax
---

<div class="title"><div></div><div>

# Introducing Marp slides
*A new Codestar theme for Marp*

</div></div>

---

<center>

Scan to follow along or keep the link for later:

<!-- Update this link with the name of your slides instead of 'example' -->
![w:256px](https://api.qrserver.com/v1/create-qr-code/?data=slides.codestar.nl/example/&size=512x512&bgcolor=f1e7da&margin=16)

*Link to the slides*

</center>

---

## this is what title<br>cards look like

Optional sub-title

<!-- Presenter notes are derived from HTML comments -->

---

![bg left:33%](https://picsum.photos/1080?image=20)

A slide with a split background

---

![bg right:33%](https://picsum.photos/1080?image=2)

It can also go to the right

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg vertical](https://fakeimg.pl/1920x360/a560a8/fff/?text=Vertically)
![bg](https://fakeimg.pl/1920x360/b56eb8/fff/?text=split)
![bg](https://fakeimg.pl/1920x360/c97ccc/fff/?text=background!)

---

## Bullet lists

---

<div class="columns">
<div>

Here are some bullets:

- One
  - A
  - B
- Two
- Three

</div>
<div>

And numbered:

1. Foo
1. Bar
1. Baz

</div>
</div>

---

## Fragmented list

---

<div class="columns">
<div>

Here are some incremental bullets:

* One
* Two
* Three

</div>
<div>

And numbered:

1) Foo
2) Bar
3) Baz

</div>
</div>

---

## formatting options

---

<!-- _footer: That guy is doing some serious business -->

![bg opacity:.1](https://picsum.photos/1080?image=5)

**bold!** _italic!_ emoji codes: :satellite: :otter:

link: https://github.com/code-star

Someone once said something:
> Lorem ipsum dolor sit amet, consectetur adipiscing elit.

1. First item
2. Second item

---

<!-- _transition: slide -->

## And of course,<br>some code

*With a different transition*

---

<center>

Some code

</center>

```ruby
# The Greeter class
class Greeter
  def initialize(name)
    @name = name.capitalize
  end

  def salute
    puts "Hello #{@name}!"
  end
end

g = Greeter.new("world")
g.salute
```

---

<!-- _footer: 'All the way accross the sky!' -->

<div class="columns">
<div>

Double

```scala
// The Greeter class
case class Greeter(name: String) {
  private val capitalizedName =
    name.capitalize

  def salute(): Unit = {
    println(s"Hello $capitalizedName!")
  }
}

val g = Greeter("world")
g.salute()
```

</div>
<div>

code!

```py
# The Greeter class
class Greeter:
    def __init__(self, name):
        self.name = name.capitalize()

    def salute(self):
        print(f"Hello {self.name}!")

g = Greeter("world")
g.salute()
```

</div>
</div>

---

## Other stuff

---

Inline math: $ax^2+bc+c$.

Math block:

$$ I_{xx}=\int\int_Ry^2f(x,y)\cdot{}dydx $$

Wow.

$$
f(x) =
  \int_{-\infty}^\infty
  \hat f(\xi)\,e^{2 \pi i \xi x}
  \,d\xi
$$

---

Basic:

| foo | bar |
| --- | --- |
| baz | bim |

Alignments:

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

---

## Questions time

---

<div class="thanks"></div>
