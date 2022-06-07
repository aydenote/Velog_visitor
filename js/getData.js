var cheerio = require('cheerio');
var request = require('request');
var axios = require('axios');

const log = console.log;

const getHtml = async () => {
  try {
    return await axios.get('https://velog.io/@aydenote');
  } catch (error) {
    console.error(error);
  }
};

const getLinkData = async (title) => {
  let titleForm = title.mainContents.map(val=> val.replace(/\s/g, "-"));
  for (const item of titleForm) {
    try {
      return await axios.get(`https://velog.io/@aydenote/${item}`);
    } catch (error) {
      console.error(error);
    }
  }
};
getHtml()
  .then((html) => {
    // axios 응답 스키마 `data`는 서버가 제공한 응답(데이터)을 받는다.
    // load()는 인자로 html 문자열을 받아 cheerio 객체 반환
    const $ = cheerio.load(html.data);
    const str = `${$('#root>div:nth-child(2)>div:nth-child(3)>div:nth-child(4)>div:nth-child(3)>div:first-child>div')}`;
    const arr = str.split("/@aydenote/");
    const arr1 = [];
    for(let i=1; i<21; i++){
    arr1.push(
        $(`#root>div:nth-child(2)>div:nth-child(3)>div:nth-child(4)>div:nth-child(3)>div:first-child>div:nth-child(${i})>a:nth-child(2)`).text()
    )
}

    const data = {
      mainContents: arr1,
    };
    return data;
  })
  .then((res) => getLinkData(res))
  .then((linkData)=> console.log(linkData))