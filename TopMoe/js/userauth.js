var Userauth = {
	
	//判断用户是否登录 否则跳转登录页面
	aloginfor : function(dom){
			var user = localStorage.getItem("userid");
			//if user == none
			if(user){
				alert('已登录')
			}else{
//				mui.openWindow({
//					url: 'login.html',
//					id: 'login',
//					show: {
//						aniShow: true
//					},
//					waiting: {
//						autoShow: false
//					}
//				});
			}
	}
	
}