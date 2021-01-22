import createClass from 'create-react-class';

class Sect extends React.Component {
  constructor(props) {
    super(props);
    this.state = {errors: perrors};
  }
  render () {
    return <output contentEditable = 'true'>Test</output>
  }
}

class TextBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: soln, errors: perrors};
  }
  render () {
    const final = [];
    
    for ( var element of this.state.value) {
      final.push(<Sect contentEditable='true'>{element}</Sect>)
    }
    console.log(final) 
    return <div contentEditable='true'>{final}</div>
  }
}

ReactDOM.render(<TextBox />, document.getElementById('main'));
