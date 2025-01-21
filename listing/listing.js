function truncate(s, n) {
  if (s.length <= n) return s

  const truncated = s.slice(0, n - 3);
  const lastSpace = truncated.lastIndexOf(" ");

  return (lastSpace > -1 ? truncated.slice(0, lastSpace) : truncated) + "...";
}

fetch("decks.json")
  .then(response => {
    return response.json();
  })
  .then(data => {
    const items = data.map(i => ({
      ...i,
      title: truncate(i.title, 75),
      date: i.date.replaceAll("-", "&ndash;"),
      link: window.location.href + i.path
    }))

    const options = {
      valueNames: [
        "title", "author", "date", "total_slides",
        { name: "link", attr: "href" }
      ],
      item: `
        <li>
          <a class="link deck">
            <div class="title"></div>
            <div class="author"></div>
            <div class="date"></div>
            <div class="total_slides"></div>
          </a>
        </li>
      `
    };

    const deckList = new List("decks", options, items);
  })
  .catch(error => {
    console.error("Error fetching or processing the decks list:", error);
  });
