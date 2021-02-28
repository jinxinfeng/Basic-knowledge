/**
 * JavaScript并非通过类而是直接通过构造函数来创建实例
 */
/**
 * 构造函数模式的目的就是为了创建一个自定义类，并且创建这个类的实例。
 * 构造函数模式中拥有了类和实例的概念，并且实例和实例之间是相互独立的，即实例识别。
构造函数就是一个普通的函数，创建方式和普通函数没有区别，不同的是构造函数习惯上首字母大写。
另外就是调用方式的不同，普通函数是直接调用，而构造函数需要使用new关键字来调用
 */
function Person(name, age, gender) {
    this.name = name
    this.age = age
    this.gender = gender
    this.sayName = function () {
        alert(this.name);
    }
}
var per = new Person("孙悟空", 18, "男");
function Dog(name, age, gender) {
    this.name = name
    this.age = age
    this.gender = gender
}
var dog = new Dog("旺财", 4, "雄")
console.log(per);//当我们直接在页面中打印一个对象时，事件上是输出的对象的toString()方法的返回值
console.log(dog);
/**
 * 每创建一个Person构造函数，在Person构造函数中，为每一个对象都添加了一个sayName方法，
 * 也就是说构造函数每执行一次就会创建一个新的sayName方法。这样就导致了构造函数执行一次就会创建一个新的方法，
 * 执行10000次就会创建10000个新的方法，而10000个方法都是一摸一样的，
 * 为什么不把这个方法单独放到一个地方，并让所有的实例都可以访问到呢?这就需要原型(prototype)
 */
//在JavaScript中，每当定义一个函数数据类型(普通函数、类)时候，
//都会天生自带一个prototype属性，这个属性指向函数的原型对象，并且这个属性是一个对象数据类型的值。
/**
 * 原型对象就相当于一个公共的区域，所有同一个类的实例都可以访问到这个原型对象，我们可以将对象中共有的内容，统一设置到原型对象中。
 */
/**
 * 每一个对象数据类型(普通的对象、实例、prototype......)也天生自带一个属性__proto__，
 * 属性值是当前实例所属类的原型(prototype)。
 * 原型对象中有一个属性constructor, 它指向函数对象。
 * 在JavaScript中万物都是对象，对象和对象之间也有关系，并不是孤立存在的。对象之间的继承关系，
 * 在JavaScript中是通过prototype对象指向父类对象，
 * 直到指向Object对象为止，这样就形成了一个原型指向的链条，专业术语称之为原型链
 * 当我们访问对象的一个属性或方法时，它会先在对象自身中寻找，如果有则直接使用，
 * 如果没有则会去原型对象中寻找，如果找到则直接使用。
 * 如果没有则去原型的原型中寻找,直到找到Object对象的原型，
 * Object对象的原型没有原型，如果在Object原型中依然没有找到，则返回undefined。
 * Object是JS中所有对象数据类型的基类(最顶层的类)在Object.prototype上没有__proto__这个属性
 */