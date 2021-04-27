// 声明入口的组件
var App = {
	template:`<div>我是入口组件</div>`
};

// 声明并导出
export var num = 2; //作为一整个对象的key抛出

// 声明在导出
var num2 = 4;
export {num2}

// 抛出一个函数
export function add(x,y) {
	return console.log(x+y);
}
// 先抛出
export default App;