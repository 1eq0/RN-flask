import React, {useEffect, useState} from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ActivityIndicator, FlatList, Image } from 'react-native';
import {WebView} from 'react-native-webview';

export default function App() {

  const handleOnMessage = (e)=>{
    console.log(e.nativeEvent.data);
  };

  return (
    <View style={styles.container}>
      <WebView
        source={{uri:"http://localhost:8888/video_feed"}}
        onMessage={handleOnMessage}
        javaScriptEnabled={true}
        automaticallyAdjustContentInsets={false}
        style={{flex:1,width:400}}
      />
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
