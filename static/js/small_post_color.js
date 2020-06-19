    var like = document.getElementById("like")
    var dislike = document.getElementById("dislike")
    var collect = document.getElementById("collect")
    like.getAttribute("data-b");
    dislike.getAttribute("data-b");
    collect.getAttribute("data-b");
    if (like.dataset.b == 1)
        like.style.color = "dimgray"
    else like.style.color = "white"
    if (dislike.dataset.b == 1)
        dislike.style.color = "dimgray"
    else dislike.style.color = "white"
    if (collect.dataset.b == 1)
        collect.style.color = "dimgray"
    else collect.style.color = "white"