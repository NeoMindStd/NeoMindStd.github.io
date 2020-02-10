var visibleLinks = document.getElementById("visible-links");
var hiddenLinks = document.getElementById("hidden-links");
var linksSize = visibleLinks.childElementCount + hiddenLinks.childElementCount;
var links = [];
for(var i=0; i<linksSize; i++) links.push(document.getElementById("head-"+i));
for(var i=0; i<linksSize; i++) {
    if(links[i].className=='dropdown'){
        links[i].children[1].style.setProperty(`--text`,`translateX(-50%)`);
    }
}
var observer = new MutationObserver(function(){
    for(var i=0; i < linksSize - hiddenLinks.childElementCount; i++){
        if(links[i].className=='dropdown'){
            links[i].children[1].style.setProperty(`--text`,`translateX(-50%)`);
        }
    }
    for(var i=linksSize - hiddenLinks.childElementCount; i < linksSize; i++){
        if(links[i].className=='dropdown'){
            links[i].children[1].style.setProperty(`--text`,`translateX(-200%)`);
        }
    }
});
observer.observe(hiddenLinks, { attributes: false, childList: true });