function login_user(username, userid, useremail){
	localStorage.setItem('userid', userid)
	localStorage.setItem('username', username)
	localStorage.setItem('useremail', useremail)
}

function logout_user(userid){
	storage.clear()
}

function auth_logintype(){
	var userid = localStorage.getItem("userid");
	if(user){
		return null;
	}else{
		return userid
	}
}