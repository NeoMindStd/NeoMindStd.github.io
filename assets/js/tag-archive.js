(function () {
  const resultsEl = document.getElementById("nm-tag-results");
  const cloudEl = document.getElementById("nm-tag-cloud");
  const browserEl = document.getElementById("nm-tag-browser");
  const cloudWrapEl = document.getElementById("nm-tag-cloud-wrap");
  const toggleBtn = document.getElementById("nm-tag-toggle");
  const toggleLabelEl = document.getElementById("nm-tag-toggle-label");
  const toggleMetaEl = document.getElementById("nm-tag-toggle-meta");
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
    const hash = url.hash || "";
    if (hash.indexOf("#tag=") === 0) {
      return decodeURIComponent(hash.slice(5));
    }
    return url.searchParams.get("tag");
  }

  function setSelectedTag(tag) {
    const url = new URL(window.location.href);
    url.searchParams.delete("tag");
    url.hash = tag ? "tag=" + encodeURIComponent(tag) : "";
    window.history.pushState({}, "", url);
  }

  function normalizeLegacyTagUrl() {
    const url = new URL(window.location.href);
    const queryTag = url.searchParams.get("tag");
    if (!queryTag) {
      return;
    }
    url.searchParams.delete("tag");
    url.hash = "tag=" + encodeURIComponent(queryTag);
    window.history.replaceState({}, "", url);
  }

  function setCloudCollapsed(collapsed, tag) {
    if (!browserEl || !cloudWrapEl || !toggleBtn) {
      return;
    }

    browserEl.classList.toggle("is-collapsed", collapsed);
    cloudWrapEl.hidden = collapsed;
    toggleBtn.setAttribute("aria-expanded", String(!collapsed));

    if (toggleLabelEl) {
      toggleLabelEl.textContent = collapsed ? "태그 목록 펼치기" : "태그 목록 접기";
    }

    if (toggleMetaEl) {
      toggleMetaEl.textContent = tag
        ? '선택된 태그: "' + tag + '"'
        : "총 " + chips.length + "개 태그";
    }
  }

  function scrollResultsIntoView() {
    window.requestAnimationFrame(() => {
      resultsEl.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  function scrollTagBrowserIntoView() {
    if (!browserEl) {
      return;
    }

    window.requestAnimationFrame(() => {
      browserEl.scrollIntoView({ behavior: "smooth", block: "start" });
    });
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
        ? '<p class="page__meta">카테고리: ' + escapeHtml(post.categories.join(", ")) + '</p>'
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
      '  <div class="nm-tag-results__summary">',
      '    <h2 class="archive__subtitle">' + escapeHtml(tag) + '</h2>',
      '    <p class="nm-tag-results__meta">총 ' + posts.length + '개 글</p>',
      '  </div>',
      '  <button type="button" class="nm-tag-results__show-list" data-tag-show-list>태그 목록 다시 보기</button>',
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
            throw new Error("태그 데이터를 불러오지 못했습니다.");
          }
          return response.json();
        });
    }
    return tagIndexPromise;
  }

  async function renderSelectedTag(tag, options = {}) {
    const shouldScroll = Boolean(options.scrollToResults);
    markActiveChip(tag);

    if (!tag) {
      setCloudCollapsed(false, null);
      renderMessage("info", "태그를 선택하면 해당 태그의 포스트만 불러옵니다.");
      return;
    }

    setCloudCollapsed(true, tag);
    renderMessage("info", '"' + tag + '" 태그 글을 불러오는 중입니다.');
    if (shouldScroll) {
      scrollResultsIntoView();
    }

    try {
      const data = await loadIndex();
      const posts = data.tags && data.tags[tag] ? data.tags[tag] : [];
      if (!posts.length) {
        renderMessage("warning", '"' + tag + '" 태그에는 아직 포스트가 없습니다.');
        if (shouldScroll) {
          scrollResultsIntoView();
        }
        return;
      }
      renderPosts(tag, posts);
      if (shouldScroll) {
        scrollResultsIntoView();
      }
    } catch (error) {
      renderMessage("danger", error.message || "목록을 불러오지 못했습니다.");
      if (shouldScroll) {
        scrollResultsIntoView();
      }
    }
  }

  if (toggleBtn) {
    toggleBtn.addEventListener("click", function () {
      const collapsed = browserEl ? browserEl.classList.contains("is-collapsed") : false;
      const nextCollapsed = !collapsed;
      setCloudCollapsed(nextCollapsed, getSelectedTag());

      if (!nextCollapsed) {
        scrollTagBrowserIntoView();
      }
    });
  }

  chips.forEach((chip) => {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      const tag = chip.dataset.tag;
      setSelectedTag(tag);
      renderSelectedTag(tag, { scrollToResults: true });
    });
  });

  resultsEl.addEventListener("click", function (event) {
    const showListBtn = event.target.closest("[data-tag-show-list]");
    if (!showListBtn) {
      return;
    }

    setCloudCollapsed(false, getSelectedTag());
    scrollTagBrowserIntoView();
    if (toggleBtn) {
      toggleBtn.focus({ preventScroll: true });
    }
  });

  window.addEventListener("popstate", function () {
    renderSelectedTag(getSelectedTag());
  });

  window.addEventListener("hashchange", function () {
    renderSelectedTag(getSelectedTag());
  });

  normalizeLegacyTagUrl();
  renderSelectedTag(getSelectedTag());
})();
