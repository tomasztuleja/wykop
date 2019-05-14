document.addEventListener("DOMContentLoaded",() => {
  let nsfw_buttons = document.getElementsByClassName('nsfw-button')

  for(let i = 0; i < nsfw_buttons.length; i++) {
    nsfw_buttons[i].onclick = (e) => {

      const id = e.target.dataset.id
      const content = document.getElementsByClassName('nsfw-content')
      
      for (let i = 0; i < content.length; i++) {        
        let element = content[i]
        if (element.dataset.id = id) {
          element.style.display = "block"
          e.target.style.display = "none"
        }
      };
      
    }
  }
})
