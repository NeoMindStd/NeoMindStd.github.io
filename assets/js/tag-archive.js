(function () {
  const resultsEl = document.getElementById("nm-tag-results");
  const cloudEl = document.getElementById("nm-tag-cloud");
  if (!resultsEl || !cloudEl) {
    return;
  }

  const chips = Array.from(cloudEl.querySelectorAll(".nm-tag-chip"));
  const indexUrl = resultsEl.getAttribute("data-index-url");
  let tagIndexPromise = null;

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function getSelectedTag() {
    const url = new URL(window.location.href);
    return url.searchParams.get("tag");
  }

  function setSelectedTag(tag) {
    const url = new URL(window.location.href);
    if (tag) {
      url.searchParams.set("tag", tag);
    } else {
      url.searchParams.delete("tag");
    }
    window.history.pushState({}, "", url);
  }

  function markActiveChip(tag) {
    chips.forEach((chip) => {
      chip.classList.toggle("is-active", chip.dataset.tag === tag);
    });
  }

  function renderMessage(type, message) {
    resultsEl.innerHTML = '<div class="notice--' + type + '">' + escapeHtml(message) + '</div>';
  }

  function renderPosts(tag, posts) {
    const items = posts.map((post) => {
      const excerpt = post.excerpt ? '<p class="archive__item-excerpt">' + escapeHtml(post.excerpt) + '</p>' : "";
      const categories = Array.isArray(post.categories) && post.categories.length
        ? '<p class="page__meta">????: ' + escapeHtml(post.categories.join(", ")) + '</p>'
        : "";
      return [
        '<div class="list__item">',
        '  <article class="archive__item">',
        '    <h2 class="archive__item-title no_toc"><a href="' + escapeHtml(post.url) + '">' + escapeHtml(post.title) + '</a></h2>',
        '    <p class="page__meta">' + escapeHtml(post.date) + '</p>',
        categories,
        excerpt,
        '  </article>',
        '</div>'
      ].join("\n");
    }).join("\n");

    resultsEl.innerHTML = [
      '<div class="nm-tag-results__header">',
      '  <h2 class="archive__subtitle">' + escapeHtml(tag) + '</h2>',
      '  <p class="nm-tag-results__meta">? ' + posts.length + '?? ?</p>',
      '</div>',
      '<div class="entries-list">',
      items,
      '</div>'
    ].join("\n");
  }

  async function loadIndex() {
    if (!tagIndexPromise) {
      tagIndexPromise = fetch(indexUrl, { headers: { Accept: "application/json" } })
        .then((response) => {
          if (!response.ok) {
            throw new Error("?? ???? ???? ?????.");
          }
          return response.json();
        });
    }
    return tagIndexPromise;
  }

  async function renderSelectedTag(tag) {
    markActiveChip(tag);

    if (!tag) {
      renderMessage("info", "??? ???? ?? ??? ?? ?????.");
      return;
    }

    renderMessage("info", '"' + tag + '" ?? ?? ???? ????.');

    try {
      const data = await loadIndex();
      const posts = data.tags && data.tags[tag] ? data.tags[tag] : [];
      if (!posts.length) {
        renderMessage("warning", '"' + tag + '" ??? ???? ?? ?? ?????.');
        return;
      }
      renderPosts(tag, posts);
    } catch (error) {
      renderMessage("danger", error.message || "?? ?? ???? ?????.");
    }
  }

  chips.forEach((chip) => {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      const tag = chip.dataset.tag;
      setSelectedTag(tag);
      renderSelectedTag(tag);
    });
  });

  window.addEventListener("popstate", function () {
    renderSelectedTag(getSelectedTag());
  });

  renderSelectedTag(getSelectedTag());
})();
