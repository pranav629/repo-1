// email_service/server.js
const express = require('express');
const nodemailer = require('nodemailer');
const app = express();
app.use(express.json());

app.post('/send-email', async (req, res) => {
  const { to, subject, message } = req.body;

  try {
    let transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: 'startupconnect8@gmail.com',
        pass: 'dbtp ksln ldhk gwje' // NOT your Gmail password
      }
    });

    let info = await transporter.sendMail({
      from: 'startupconnect8@gmail.com',
      to,
      subject,
      text: message
    });

    res.json({ success: true, message: 'Email sent!', info });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(5000, () => {
  console.log('Node.js email server running on port 5000');
});
