let content_feild = document.getElementById("content_feild")

let image = document.createElement("input").name = "src"
let heading  = document.createElement("input").name = "Title"
let text = document.createElement("textarea").name = "content"
let new_part = document.createElement("hr")

function add_img(){
    content_feild.appendChild(image)
}