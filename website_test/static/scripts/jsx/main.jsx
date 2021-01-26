import React, { useState } from 'react';


function Sect(props) {
  return (
    <output>{props.chunk}</output>
  )
} 

function TextBox() {
  const [isShown, setIsShown] = useState(false);
  const final = [];
  for (const element of soln) {
    final.push(<Sect contentEditable='true' chunk={element}></Sect>)
  }

  return(<div contentEditable = 'true' >{true && final}</div>)
}
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

ReactDOM.render(<TextBox></TextBox>, document.getElementById('main'));
