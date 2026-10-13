// Hành vi của landing: hiện dần khi cuộn tới, tab case study, chép lệnh.
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

// Thứ tự xuất hiện của phần tử con, đọc qua biến --i trong CSS.
const setOrder = (items) => items.forEach((item, index) => item.style.setProperty("--i", index));
setOrder([...document.querySelectorAll("[data-hero] > *")]);
for (const group of document.querySelectorAll("[data-stagger], [data-chat], [data-result]")) setOrder([...group.children]);
for (const panel of document.querySelectorAll("[data-panel]")) {
  const chatCount = panel.querySelector("[data-chat]")?.children.length ?? 0;
  panel.querySelector("[data-result]")?.style.setProperty("--n", chatCount);
}

// Phát lại hội thoại: bỏ lớp rồi gắn lại ở khung hình sau để animation chạy từ đầu.
const play = (panel) => {
  if (reduceMotion || !panel) return;
  panel.classList.remove("is-playing");
  requestAnimationFrame(() => requestAnimationFrame(() => panel.classList.add("is-playing")));
};

const observer = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    if (!entry.isIntersecting) continue;
    entry.target.classList.add("is-visible");
    if (entry.target.id === "case") play(entry.target.querySelector("[data-panel]:not([hidden])"));
    observer.unobserve(entry.target);
  }
}, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
for (const section of document.querySelectorAll("[data-reveal]")) observer.observe(section);

// Tab case study: bấm hoặc phím mũi tên trái phải.
const tabs = [...document.querySelectorAll("[data-case]")];
const selectTab = (tab, focus = false) => {
  for (const other of tabs) {
    const selected = other === tab;
    other.setAttribute("aria-selected", String(selected));
    other.tabIndex = selected ? 0 : -1;
    document.getElementById(other.getAttribute("aria-controls")).hidden = !selected;
  }
  if (focus) tab.focus();
  play(document.getElementById(tab.getAttribute("aria-controls")));
};
for (const tab of tabs) {
  tab.tabIndex = tab.getAttribute("aria-selected") === "true" ? 0 : -1;
  tab.addEventListener("click", () => selectTab(tab));
  tab.addEventListener("keydown", (event) => {
    const step = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
    if (!step) return;
    event.preventDefault();
    selectTab(tabs[(tabs.indexOf(tab) + step + tabs.length) % tabs.length], true);
  });
}

// Chép lệnh: đổi icon thành dấu ✓ trong 1,5 giây.
for (const button of document.querySelectorAll("[data-copy]")) {
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
    } catch {
      return;
    }
    button.setAttribute("data-copied", "");
    button.setAttribute("aria-label", "Đã chép");
    setTimeout(() => {
      button.removeAttribute("data-copied");
      button.setAttribute("aria-label", "Chép lệnh");
    }, 1500);
  });
}
