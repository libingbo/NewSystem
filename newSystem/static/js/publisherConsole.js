function addNew()
{
    var iframe = document.getElementById('iframe_a');
    //获取当前网址
    var a =window.document.location.href;
    // 127.0.0.1:8000就等价于.idea下面那个newSystem文件夹
    iframe.setAttribute("src" , "http://127.0.0.1:8000/static/localHtml/addNew.html" );
}