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

import createClass from 'create-react-class';

var Hello = createClass({
  render: function() {
      return <div>Hello, { soln }!</div>;
  }
});

ReactDOM.render(<Hello />, document.getElementById('main'));
