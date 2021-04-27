import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const store =  new Vuex.Store({
	// 五大将  state  mutation action getter  module
	state:{
		count:1
	},
	mutations:{
		// 修改状态 更改 Vuex 的 store 中的状态state的唯一方法是提交(commit) mutation
		// 方法
		// 只能做同步操作 不能 直接commit
		// 同步
		addCount(state,val){
			state.count+=val;
		},
		// 同步
		asyncHandler(state,val){
			state.count+=val;
		}
	},
	actions:{

// Action 类似于 mutation，不同在于：

// Action 提交 mutation，而不是直接变更状态。
// Action 可以包含任意异步操作。
		asyncHandler({commit},val){
			commit('asyncHandler',val)
		},
		addCount({commit},val){
			setTimeout(()=>{
				commit('addCount',val)
			},2000)
		}

	}
});

export default store;