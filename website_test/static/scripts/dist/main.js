"use strict";

var _createReactClass = _interopRequireDefault(require("create-react-class"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

//ReactDOM.render(
//  <h1>This is, {window.obj}</h1>,
//  document.getElementById('main')
//);

/*
ReactDOM.render(
  <p>{solution}</p>,
  document.getElementById('main')
);
*/
var Hello = (0, _createReactClass["default"])({
  render: function render() {
    return /*#__PURE__*/React.createElement("div", null, "Hello, ", soln, "!");
  }
});
ReactDOM.render( /*#__PURE__*/React.createElement(Hello, null), document.getElementById('main'));