document$.subscribe(function () {
  // Remove any giscus script tags we previously injected (SPA navigation cleanup)
  document.querySelectorAll('script[data-giscus-inserted]').forEach(function (el) {
    el.remove();
  });

  var article =
    document.querySelector('article.md-content__inner') ||
    document.querySelector('.md-content__inner');
  if (!article) return;

  var container = document.createElement('div');
  container.className = 'giscus';
  article.appendChild(container);

  var script = document.createElement('script');
  script.src = 'https://giscus.app/client.js';
  script.setAttribute('data-giscus-inserted', '1');
  script.setAttribute('data-repo', 'Culinary-Projects/The-52-Week-Culinary-Project');
  script.setAttribute('data-repo-id', 'R_kgDORh35DQ');
  script.setAttribute('data-category', 'General');
  script.setAttribute('data-category-id', 'DIC_kwDORh35Dc4C5IwP');
  script.setAttribute('data-mapping', 'pathname');
  script.setAttribute('data-strict', '0');
  script.setAttribute('data-reactions-enabled', '1');
  script.setAttribute('data-emit-metadata', '0');
  script.setAttribute('data-input-position', 'bottom');
  script.setAttribute('data-theme', 'preferred_color_scheme');
  script.setAttribute('data-lang', 'en');
  script.setAttribute('crossorigin', 'anonymous');
  script.async = true;
  document.head.appendChild(script);
});
