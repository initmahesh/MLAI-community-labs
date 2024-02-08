import React from 'react';

function TextWithLineBreaks(props) {
  const textWithBreaks = props.text.split('\n').map((text, index) => (
    <React.Fragment key={index}>
      {text}
      <br />
    </React.Fragment>
  ));

  return <div>{textWithBreaks}</div>;
}

export default TextWithLineBreaks;