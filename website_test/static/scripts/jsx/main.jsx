//import React, { useState } from 'react';


/*
function Sect(props) {
  return (
    <output>{props.chunk}</output>
  )
}
*/

class Text extends React.Component {

  render() {
    return <output>{this.props.chunk}</output>
  }
}

class Error extends React.Component {

  constructor(props) {
    super(props);
    this.state = {isShown: false};
  }

  hoverOn() {
    this.setState(state => ({
      isShown: true
    }));
  }

  hoverOff() {
    this.setState(state => ({
      isShown: false
    }));
  }

  render() {
    //return <output>{this.props.chunk}</output>
    return(<div onMouseEnter={this.hoverOn.bind(this)}
    onMouseLeave={this.hoverOff.bind(this)} contentEditable = 'true' >{this.state.isShown && this.props.chunk}</div>)
  }
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

class TextBox extends React.Component {

  // constructor(props) {
  //  super(props);
  //  this.state = {isShown: false};

    // This binding is necessary to make `this` work in the callback
    // this.hoverOff = this.hoverOff.bind(this);
    // this.hoverOn = this.hoverOn.bind(this);
  // }

  // hoverOn() {
  //   this.setState(state => ({
  //     isShown: true
  //   }));
  // }

  // hoverOff() {
  //   this.setState(state => ({
  //     isShown: false
  //   }));
  // }

  
  render() {
    /*
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
    */
  
  const final = []
  for (const element of soln) {
    if (typeof(element) == "number" && element != -1) {
      final.push(<Error contentEditable='true' chunk={element}></Error>)
    }
    if (typeof(element) == "string") {
      final.push(<Text contentEditable='true' chunk={element}></Text>)
    }
    
  }

  // return(<div onMouseEnter={this.hoverOn.bind(this)}
  // onMouseLeave={this.hoverOff.bind(this)} contentEditable = 'true' >{this.state.isShown && final}</div>)

  return(<div contentEditable = 'true'>{final}</div>)
  }
}
  


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

ReactDOM.render(<TextBox></TextBox>, document.getElementById('main'));
// class TextBox extends React.Component {
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