function xhrHttp(data) {
                //创建ajax对象
    var xhr = new XMLHttpRequest();

    //配置这个对象open
    //参数：
    //1. 请求的方式: (string) get/post
    //2. 请求的路径：(string) url
    //3. 请求是否异步: (boolean) true为异步
    xhr.open('get', '/blog/addArticla', true);

    //监听响应：
    xhr.onreadystatechange = function () {
        //这个事件，在xhr.readyState发生变化时，会触发。
        //xhr.readyState:0 ,xhr对象刚刚创建
        //xhr.readyState 0 ===> 1, xhr调用了open方法
        //xhr.readyState 1 ===> 2, xhr调用了send方法
        //xhr.readyState 2 ===> 3, 当服务器返回了部分数据
        //xhr.readyState 3 ===> 4, 当服务器返回了全部数据
        if (xhr.readyState !== 4) {
            return;
        }

        //此时，说明服务器已经返回了响应，我们需要判断响应的结果
        if (xhr.status >= 200 && xhr.status <= 300) {
            //服务器的响应码是200到300之间，说明响应成功
            // 取得数据
            alert(xhr.responseText);
        } else {
            //响应失败
            console.error('请求失败');
        }
    }

    //发送请求
    xhr.send();
}

        var btn = document.querySelector('button')
		btn.addEventListener('click',function(){
			xhrHttp()

		},false)

