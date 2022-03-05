const dis = document.querySelector(".display");
const text = document.querySelector(".textarea");
const submitD = document.querySelector(".submit");
const homeD = document.querySelector(".home");

submitD.addEventListener("click", () => {
  text_to = text.value;
  dis.innerHTML = text_to;
});
