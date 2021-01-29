(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
"use strict";

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

function _createForOfIteratorHelper(o, allowArrayLike) { var it; if (typeof Symbol === "undefined" || o[Symbol.iterator] == null) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = o[Symbol.iterator](); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } return _assertThisInitialized(self); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Date.prototype.toString.call(Reflect.construct(Date, [], function () {})); return true; } catch (e) { return false; } }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }

//import React, { useState } from 'react';
function Sect(props) {
  return /*#__PURE__*/React.createElement("output", null, props.chunk);
}
/*
function TextBox() {
  const [shown, setShown] = useState(false);
  const final = [];
  for (const element of soln) {
    final.push(<Sect contentEditable='true' chunk={element}></Sect>)
  }

  return(<div onMouseEnter={() => setShown(true)}
           onMouseLeave={() => setShown(false)} contentEditable = 'true' >{shown && final}</div>)
}
*/


var TextBox = /*#__PURE__*/function (_React$Component) {
  _inherits(TextBox, _React$Component);

  var _super = _createSuper(TextBox);

  function TextBox(props) {
    var _this;

    _classCallCheck(this, TextBox);

    _this = _super.call(this, props);
    _this.state = {
      isShown: false
    }; // This binding is necessary to make `this` work in the callback
    // this.hoverOff = this.hoverOff.bind(this);
    // this.hoverOn = this.hoverOn.bind(this);

    return _this;
  }

  _createClass(TextBox, [{
    key: "hoverOn",
    value: function hoverOn() {
      this.setState(function (state) {
        return {
          isShown: true
        };
      });
    }
  }, {
    key: "hoverOff",
    value: function hoverOff() {
      this.setState(function (state) {
        return {
          isShown: false
        };
      });
    }
  }, {
    key: "render",
    value: function render() {
      /*
      return (
        <button onClick={this.handleClick}>
          {this.state.isToggleOn ? 'ON' : 'OFF'}
        </button>
      );
      */
      var _final = [];

      var _iterator = _createForOfIteratorHelper(soln),
          _step;

      try {
        for (_iterator.s(); !(_step = _iterator.n()).done;) {
          var element = _step.value;

          _final.push( /*#__PURE__*/React.createElement(Sect, {
            contentEditable: "true",
            chunk: element
          }));
        }
      } catch (err) {
        _iterator.e(err);
      } finally {
        _iterator.f();
      }

      return /*#__PURE__*/React.createElement("div", {
        onMouseEnter: this.hoverOn.bind(this),
        onMouseLeave: this.hoverOff.bind(this),
        contentEditable: "true"
      }, this.state.isShown && _final);
    }
  }]);

  return TextBox;
}(React.Component);
/*
  render () {
    const final = [];
    
    for ( const element of this.state.value) {
      final.push(<Sect contentEditable='true' chunk={element}></Sect>)
    }
    console.log(final)
    return <div contentEditable='true'
    onMouseEnter={() => setIsShown(true)}
        onMouseLeave={() => setIsShown(false)}>{final}</div>
  }
}
*/


ReactDOM.render( /*#__PURE__*/React.createElement(TextBox, null), document.getElementById('main')); // class TextBox extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {value: soln, errors: perrors, isShown: false, setisShown: false};
//   }
//   render () {
//     const final = [];
//     for ( const element of this.state.value) {
//       final.push(<Sect contentEditable='true' chunk={element}></Sect>)
//     }
//     console.log(final)
//     return <div contentEditable='true'
//     onMouseEnter={() => setIsShown(true)}
//         onMouseLeave={() => setIsShown(false)}>{final}</div>
//   }
// }
},{}]},{},[1]);
