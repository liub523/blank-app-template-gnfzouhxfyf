import streamlit as st

# 设置页面标题
st.title("NMOS SDP文件参数生成器")

# 左侧参数设置
st.sidebar.header("设置参数")
version = st.sidebar.text_input("SDP版本", "v=0")
origin = st.sidebar.text_input("会话发起者", "- 0 0 IN IP4 192.168.1.1")
session_name = st.sidebar.text_input("会话名称", "NMOS SDP示例")
time_description = st.sidebar.text_input("时间描述", "t=0 0")

# 视频流参数
st.sidebar.header("视频流参数")
video_port = st.sidebar.number_input("视频端口", min_value=1024, max_value=65535, value=5000)
video_ip = st.sidebar.text_input("视频IP地址", "192.168.1.1")
video_encoding = st.sidebar.text_input("视频编码格式", "H264")
video_rtp_map = st.sidebar.text_input("视频RTP映射", "96")
video_attributes = st.sidebar.text_area("视频其他属性", "a=control:video")

# 音频流参数
st.sidebar.header("音频流参数")
audio_port = st.sidebar.number_input("音频端口", min_value=1024, max_value=65535, value=5002)
audio_ip = st.sidebar.text_input("音频IP地址", "192.168.1.1")
audio_encoding = st.sidebar.text_input("音频编码格式", "AAC")
audio_rtp_map = st.sidebar.text_input("音频RTP映射", "97")
audio_attributes = st.sidebar.text_area("音频其他属性", "a=control:audio")

# 辅助数据流参数
st.sidebar.header("辅助数据流参数")
data_port = st.sidebar.number_input("辅助数据端口", min_value=1024, max_value=65535, value=5004)
data_ip = st.sidebar.text_input("辅助数据IP地址", "192.168.1.1")
data_encoding = st.sidebar.text_input("辅助数据编码格式", "application/octet-stream")
data_rtp_map = st.sidebar.text_input("辅助数据RTP映射", "98")
data_attributes = st.sidebar.text_area("辅助数据其他属性", "a=control:data")

# 生成SDP文件文本
sdp_content = f"""
{version}
o={origin}
s={session_name}
{time_description}
"""

# 视频流
sdp_content += f"""
m=video {video_port} RTP/AVP {video_rtp_map}
c=IN IP4 {video_ip}
a=rtpmap:{video_rtp_map} {video_encoding}/90000
{video_attributes}
"""

# 音频流
sdp_content += f"""
m=audio {audio_port} RTP/AVP {audio_rtp_map}
c=IN IP4 {audio_ip}
a=rtpmap:{audio_rtp_map} {audio_encoding}/48000
{audio_attributes}
"""

# 辅助数据流
sdp_content += f"""
m=application {data_port} RTP/AVP {data_rtp_map}
c=IN IP4 {data_ip}
a=rtpmap:{data_rtp_map} {data_encoding}/90000
{data_attributes}
"""

# 右侧显示生成的SDP文件文本
st.header("生成的SDP文件文本")
st.text_area("SDP文件", sdp_content, height=400)

# 运行应用
if __name__ == "__main__":
    st.run()
