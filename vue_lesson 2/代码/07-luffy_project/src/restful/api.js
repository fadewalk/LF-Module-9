
import Axios  from 'axios'
// 设置公共的url
Axios.defaults.baseURL = 'https://www.luffycity.com/api/v1/';

// 添加请求拦截器
Axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    if (localStorage.getItem('access_token')) {
    	// Axios.defaults.headers.common['Authorization'] = localStorage.getItem('access_token');
    	// console.log(config.headers);
    	config.headers.Authorization = localStorage.getItem('access_token')
    }
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });
// 分类列表api
export const categoryList =  ()=> {
	return Axios.get('course_sub/category/list/').then(res=>res.data);
}
// https://www.luffycity.com/api/v1/courses/?sub_category=0
export const  allCategoryList = (categoryId)=>{
	return Axios.get(`courses/?sub_category=${categoryId}`).then(res=>res.data);
}
// 课程详情顶部数据
export const coursedetailtop = (courseid)=>{
	return Axios.get(`coursedetailtop/?courseid=${courseid}`).then(res=>res.data);
}
// 课程概述
export const coursedetail = (courseid)=>{
	return Axios.get(`coursedetail/?courseid=${courseid}`).then(res=>res.data);
}

// geetest接口
export const geetest = ()=>{
	return Axios.get(`captcha_check/`).then(res=>res.data);
}

// 登录
export const  userLogin = (params)=>{
	// 这个参数至少有五个字段 username password  验证的三个字段
	return Axios.post('account/login/',params).then(res=>res.data);
}
// 加入购物车的接口
export const shopCart = (params)=>{
	return Axios.post('user/shop_cart/create/',params).then(res=>res.data);
}
// 购物车的数据
export const shopCartList = ()=>{
	return Axios.get(`user/shop_cart/list/`).then(res=>res.data);
}
