import React, {useEffect, useState} from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ActivityIndicator, FlatList, Image } from 'react-native';
import {WebView} from 'react-native-webview';

export default function App() {

  const [reps, setReps] = useState(0);

  const handleOnMessage = (e)=>{
    console.log(e.nativeEvent.data);
  };

  const getReps = async () => {
    try{
      const response = await fetch("http://localhost:8000/reps");
      const json = await response.json();
      setReps(json.data);
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(()=>{setInterval(()=>{
    getReps(),1000
  })}
  );

  return (
    <View style={styles.container}>
      <WebView
        source={{uri:"http://localhost:8000/video_feed"}}
        onMessage={handleOnMessage}
        javaScriptEnabled={true}
        automaticallyAdjustContentInsets={false}
        style={{flex:2,width:400}}
      />
      <Text style={{flex:1}}>{reps}</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent:'center',
  },
});
