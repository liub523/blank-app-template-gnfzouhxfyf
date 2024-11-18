import streamlit as st

# SDP文件生成函数
def generate_sdp(attributes):
    sdp_content = f"v=0\n"
    sdp_content += f"o={attributes['origin']}\n"
    sdp_content += f"s={attributes['session_name']}\n"
    sdp_content += f"i={attributes['session_info']}\n"
    sdp_content += f"u={attributes['uri']}\n"
    sdp_content += f"e={attributes['email']}\n"
    sdp_content += f"p={attributes['phone']}\n"
    sdp_content += f"c=IN IP4 {attributes['connection_address']}\n"
    sdp_content += f"t=0 0\n"
    sdp_content += f"a=tool:{attributes['tool']}\n"
    sdp_content += f"a=recvonly\n"
    
    # 添加媒体描述
    sdp_content += f"m={attributes['media_type']} {attributes['port']} {attributes['protocol']} {attributes['media_format']}\n"
    sdp_content += f"a=sendrecv\n"
    
    # 添加带宽信息
    sdp_content += f"b=AS:{attributes['bandwidth']}\n"
    
    # 添加时间戳
    sdp_content += f"t={attributes['start_time']} {attributes['end_time']}\n"
    
    # 添加Dash-7属性
    sdp_content += f"a=dash-7:{attributes['dash_7']}\n"
    
    # 添加媒体格式参数
    sdp_content += f"a=fmtp:{attributes['media_format_type']} {attributes['resolution']} {attributes['frame_rate']} {attributes['bitrate']}\n"
    
    return sdp_content

# Streamlit界面
st.title("SDP 文件生成器")

# 左侧属性输入
st.sidebar.header("输入属性")
origin = st.sidebar.text_input("Origin", "User 1 0 0 IN IP4 127.0.0.1")
session_name = st.sidebar.text_input("Session Name", "SDP Session")
session_info = st.sidebar.text_input("Session Info", "This is a sample SDP session")
uri = st.sidebar.text_input("URI", "http://example.com")
email = st.sidebar.text_input("Email", "user@example.com")
phone = st.sidebar.text_input("Phone", "+123456789")
connection_address = st.sidebar.text_input("Connection Address", "192.168.1.1")
tool = st.sidebar.text_input("Tool", "SDP Generator")

# 新增媒体描述属性
media_type = st.sidebar.text_input("Media Type", "video")
port = st.sidebar.text_input("Port", "5004")
protocol = st.sidebar.text_input("Protocol", "RTP/AVP")

# 分解媒体格式属性
media_format_type = st.sidebar.text_input("Media Format Type", "96")
media_format_parameters = st.sidebar.text_input("Media Format Parameters", "parameter1=0,parameter2=1")

# 新增媒体格式参数
resolution = st.sidebar.text_input("Resolution (e.g., 1920x1080)", "1920x1080")
frame_rate = st.sidebar.text_input("Frame Rate (e.g., 30)", "30")
bitrate = st.sidebar.text_input("Bitrate (kbps)", "500")

# 新增带宽和时间戳属性
bandwidth = st.sidebar.text_input("Bandwidth (kbps)", "500")
start_time = st.sidebar.text_input("Start Time", "0")
end_time = st.sidebar.text_input("End Time", "0")

# 新增Dash-7属性
dash_7 = st.sidebar.text_input("Dash-7 Attribute", "default_value")

# 生成SDP内容
attributes = {
    "origin": origin,
    "session_name": session_name,
    "session_info": session_info,
    "uri": uri,
    "email": email,
    "phone": phone,
    "connection_address": connection_address,
    "tool": tool,
    "media_type": media_type,
    "port": port,
    "protocol": protocol,
    "media_format": f"{media_format_type} {media_format_parameters}",
    "bandwidth": bandwidth,
    "start_time": start_time,
    "end_time": end_time,
    "dash_7": dash_7,
    "media_format_type": media_format_type,
    "resolution": resolution,
    "frame_rate": frame_rate,
    "bitrate": bitrate,
}

sdp_output = generate_sdp(attributes)

# 右侧显示生成的SDP文本
st.header("生成的SDP文件")
st.text_area("SDP内容", value=sdp_output, height=300)

# 运行Streamlit应用
if __name__ == "__main__":
    st.run() 
