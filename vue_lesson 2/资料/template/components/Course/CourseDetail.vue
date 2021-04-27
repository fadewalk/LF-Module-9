<template>
	<div class="wrap">
		<div class="web-course-banner">
			<div class="container">
				<div class="title">
					<img src="../../../static/images/play.png" height="67" width="67" alt="">
					<h1 class="course-title">Django框架学习</h1>
				</div>
				<span class="course-text">Python语言下最强大优秀的WEB框架从入门到进阶</span>
				<div class="course-list">
					<ul>
					    <li class="detail-item">
					    	难度：初级
					    </li>
					    <li class="sep"></li>
					    <li class = detail-item>时长：32小时</li>
					    <li class="sep"></li>
					     <li class = detail-item>学习人数：632人</li>
					    <li class="sep"></li>
					    <li class = detail-item>评分 10.0</li>
					</ul>
				</div>
			</div>
		</div>
		<div class="course-review">
			<ul class="review-head-wrap">
				<li class="head-item">课程概述</li>
				<li class="head-item">课程章节</li>
				<li class="head-item">用户评价(10)</li>
				<li class="head-item">常见问题</li>

			</ul>
		</div>
		<!-- 课程详情 -->
		<div class="course-detail">
			<div class="container">
				<div class="course-detail-text">
					<h3>课程概述</h3>
					<p>
						Django是Python语言中最流行、最强大的WEB框架，可快速构建稳定强大的WEB项目，大大提高开发效率，很多知名项目都是基于Django开发，如Disqus、Pinterest、Instagram、Bitbucket等， Django官方Slogan是The framework for perfectionist with deadline! 一个为完美主义者且又开发工期很紧的人设计的框架，事实确实如此，Django自身集成了丰富的WEB开发通用组件，如用户认证、分页、中间件、缓存、session等，可以避免浪费大量时间重复造轮子。人生苦短，join the course now and start to build your first web program based on Django.
					</p>
				</div>
				<div class="course-img">
					<img src="https://www.luffycity.com/static/img/web-introduce.d075499.png" alt="">
				</div>
			</div>
		</div>
		<div class="course-price">
			<div class="container">
				<span>可以根据不同的学习情况购买不一样的学习套餐哦！</span>
				<ul class="course-price-item" >
					<li>
						<p class="price">¥99</p>
						<p class="time">有效期一个月</p>
					</li>
					<li>
						<p class="price">¥99</p>
						<p class="time">有效期一个月</p>
					</li>
					<li>
						<p class="price">¥99</p>
						<p class="time">有效期一个月</p>
					</li>
				</ul>
				<div class="course-action">
					<button class="left">购买</button>
					<button class="right">加入购物车</button>
				</div>
			</div>
		</div>
	
	</div>
</template>

<script>
export default {

  name: 'CourseDetail'
};
</script>

<style lang="css" scoped>
.wrap{
	width: 100%;
}
.web-course-banner{
    width: 100%;
    height: 512px;
    background: url(../../../static/images/web-banner.1402933.png) no-repeat;
    background-size: 100% 100%;
    text-align: center;
    overflow: hidden;
}
.container{
	width: 1200px;
	margin: 182px auto 0;
	text-align: left;
}
.container img{
	vertical-align: middle;
}
.container h1{
	display: inline-block;
	font-size: 48px;
    color: #4a4a4a;
    letter-spacing: .37px;
    margin-left: 40px;
    font-family: PingFangSC-Light;
    font-weight: 500;
    line-height: 1.1;
    position: relative;
    top: 10px;
}
.course-text{
    width: 464px;
    display: inline-block;
    font-size: 22px;
    color: #4a4a4a;
    letter-spacing: .17px;
    line-height: 36px;
    margin-top: 33px;
}
.course-list{
	width: 100%;
}
.course-list ul{
	margin-top: 63px;
	display: flex;
	align-items: center;
	justify-content: flex-start;
}
.course-list ul li.detail-item{
    font-size: 18px;
    color: #4a4a4a;
    letter-spacing: .74px;
    height: 26px;
    padding: 0 20px;
}
.course-list ul li.sep{
	width: 2px;
	height: 14px;
	border-left: 1px solid #979797;
}
.course-review{
	width: 100%;
	height: 80px;
	background: #fafbfc;
	border-top: 1px solid #e8e8e8;
	box-shadow: 0 1px 0 0 #e8e8e8;
}
.review-head-wrap{
	width: 590px;
	margin: 0 auto;
	display: flex;
	justify-content: space-between;
}
.review-head-wrap .head-item{
height: 80px;
    line-height: 80px;
    font-size: 16px;
    color: #555;
    cursor: pointer;
}
.course-detail{
	width: 100%;
	padding-top: 90px;

}
.course-detail .container{
	width: 1200px;
	margin: 0 auto;
	display: flex;
	justify-content:space-between;
}
.course-detail-text{
	width: 500px;
	text-align:left;

}
.course-detail-text h3{
	padding: 20px 0;
}
.course-detail-text p{
	    width: 100%;
	    height: 196px;
	    font-size: 14px;
	    color: #4A4A4A;
	    letter-spacing: 1.83px;
	    line-height: 30px;
	    text-align: left;
}
.course-price{
	width: 100%;
	background: #FAFAFA;

}
.course-price .container{
	width: 1200px;
	margin: 0 auto;
	text-align: center;
}
.course-price span{
	 font-size: 12px;
	    color: #9b9b9b;
	    letter-spacing: 1.57px;
	    display: inline-block;
	    margin-top: 102px
} 
.course-price ul{
	/*width: 800px;*/
	margin: 50px auto;

	display: flex;
	flex-wrap: wrap;
	justify-content:space-between;
}
.course-price ul li{
	width: 200px;
	height: 112px;
	border: 1px solid #979797;
}
.course-price ul li.active{
	background: #00CD23;
}
.course-price ul li p:first-child{
	font-size: 24px;
   	 letter-spacing: 1.92px;
    	color: #333;
    	margin-top: 17px;
}
.course-price ul li p:nth-child(2){

	    color: #9b9b9b;
	    font-size: 20px;
	    letter-spacing: 1.6px;
	    margin-top: 9px;
}
.course-action{
	width: 1000px;
	margin: 0 auto;
	padding-bottom: 80px;
	display: flex;
	justify-content: center;
}
.course-action button{
	border:none;
	outline: none;
	cursor: pointer;
	display: inline-block;
	width: 181px;
	    height: 51px;
	    font-size: 14px;
	    color: #fff;
	    letter-spacing: 1.12px;
	    text-align: center;
	    background: #f5a623;
	    border-radius: 82px;
}
.course-action button.left{
	background: #7ed321;
    	box-shadow: 0 2px 4px 0 #e8e8e8;
    	color: #fff;
    	margin-right: 48px;
    	padding: 0 20px;
}
.course-action button.right{
	background: #f5a623 url() no-repeat 125px 15px!important;
}

    
</style>
