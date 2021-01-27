//import React, { useState } from 'react';


function Sect(props) {
  return (
    <output>{props.chunk}</output>
  )
} 

function TextBox() {
  const [shown, setShown] = useState(false);
  const final = [];
  for (const element of soln) {
    final.push(<Sect contentEditable='true' chunk={element}></Sect>)
  }

  return(<div onMouseEnter={() => setShown(true)}
           onMouseLeave={() => setShown(false)} contentEditable = 'true' >{shown && final}</div>)
}


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