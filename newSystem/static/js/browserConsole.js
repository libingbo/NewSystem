//编辑密码
function editPassword()
{
    var iframe = document.getElementById('iframe_editPassword');
     iframe.setAttribute("src" , "http://127.0.0.1:8000/static/localHtml/editPassword.html" );
};


//更换头像
function changeHeadPhoto()
{
    var iframe = document.getElementById('iframe_editPassword');
     iframe.setAttribute("src" , "http://127.0.0.1:8000/static/localHtml/changeHeadPhoto.html" );
}


//修改信息
function editBrowserInfo()
{
    var iframe = document.getElementById('iframe_editPassword');
    iframe.setAttribute("src" , "http://127.0.0.1:8000/static/localHtml/editBrowserInfo.html");
}


