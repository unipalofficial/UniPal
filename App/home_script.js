let index = 0
let timer = null

show_content()

function show_content(){

    let feature_content = document.getElementsByClassName('feature_content')
    let content_button = document.getElementsByClassName('content_button')

    for(let i = 0; i < feature_content.length; i++){

        feature_content[i].style.display = 'none'
        content_button[i].className = content_button[i].className.replace(' active', '')

    }

    if(index >= feature_content.length) { index = 0 }

    feature_content[index].style.display = 'flex'
    content_button[index].className += ' active'

    index++

    if(timer){

        clearTimeout(timer)
        timer = null

    }

    timer = setTimeout(show_content, 6200)

}

function set_num(n){

    index = n
    show_content()

}