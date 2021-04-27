<template>
	<div class="shopping-cart-wrap">
		<h3 class="shopping-cart-tit">我的购物车<small>共1门课程</small></h3>
		<div class="row">
			<el-table
		    ref="multipleTable"
		    :data="shopCartList"
		    tooltip-effect="dark"
		    style="width: 100%"
		    @selection-change="handleSelectionChange">
		    <el-table-column
		      type="selection"
		      width="55">
		    </el-table-column>
		    <el-table-column
		      label="课程"
		      width="554">
		      <template slot-scope="scope">
		      	<img :src="scope.row.courseImg" alt="">
		      	<a href="javascript:void(0)">Django框架学习</a>
		      </template>
		    </el-table-column>
		    <el-table-column
		      prop="time"
		      label="有效期"
		      width="212">
		      <template slot-scope="scope">
		      	
		      
		      	<select>
		      		<option>有效期1个月</option>
		      		<option>有效期2个月</option>
		      		<option>有效期3个月</option>
		      	</select>
		      </template>
		    </el-table-column>
		    <el-table-column
		      prop="price"
		      label="单价"
		      show-overflow-tooltip>
		      <template slot-scope="scope">¥{{ scope.row.coursePrice}}</template>
		    </el-table-column>
		    <el-table-column
		      prop="action"
		      label="操作"
		      show-overflow-tooltip>
		      <template slot-scope="scope">
		        <el-button
		          @click.native.prevent="deleteRow(scope.$index, shopCartList)"
		          type="text"
		          size="small">
		         删除
		        </el-button>
		      </template>
		    </el-table-column>
		  </el-table>
		</div>
		<div class="total">
			<el-button type="primary">去结算</el-button>
			<h3>总计: ¥399</h3>	
		</div>
	</div>
</template>

<script>
export default {

};
</script>

<style lang="css" scoped>
.shopping-cart-wrap{
	width: 100%;
}
.shopping-cart-wrap h3,.row{
	width: 1200px;
	margin: 0 auto;
}
.shopping-cart-wrap h3{
	padding: 50px 0 ;
}
.el-table .warning-row {
	background: #22C8C5;
}
.cell img{
	vertical-align: middle;
	width: 170px;
}
.cell a{
	color: #000;
	margin-left: 30px;
}
select {
    border: 0;
    outline: none;
    font-size: 12px;
    color: #666;
    line-height: 18px;
    width: 117px;
    height: 28px;
    padding-left: 16px;
    border: 1px solid #d9d9d9;
    border-radius: 4px;
}
.total{
	width: 1200px;
	margin: 0 auto;
	/*display: flex;*/
	/*justify-content:flex-end;*/

}
.shopping-cart-wrap .total button{
	float: right;
	margin-top: 20px;
}

.shopping-cart-wrap .total h3{
	padding: 0;
	float: right;
	width: 100px;
	height: 30px;
	margin-top: 30px;
}

</style>
