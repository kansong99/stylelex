import createClass from 'create-react-class';

class TextBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: soln, errors: perrors};
  }
  render () {
    const final = [];
    
    for ( var element of this.state.value) {
      final.push(<div>{element}</div> )
    } 
    return <label> <textarea>{final}</textarea></label>
  }
}

ReactDOM.render(<TextBox />, document.getElementById('main'));
