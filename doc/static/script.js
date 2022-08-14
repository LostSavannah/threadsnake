function onReady(callback){
    document.addEventListener('DOMContentLoaded', callback, false);
}

function getHeight(selector){
    return document.querySelector(selector).offsetHeight;
}
