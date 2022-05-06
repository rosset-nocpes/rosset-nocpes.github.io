import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import Script from "next/script";       

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Sorry but our website on maintenance</title>
        <meta name="description" content="Maintenance" />
        <link
          rel="icon"
          href="https://cdn-icons.flaticon.com/png/512/5305/premium/5305390.png?token=exp=1639422002~hmac=dfc628845749712553eb322609b83284"
        />
        <script src="https://app.giveforms.com/new/widget-install.js" type="text/javascript"></script>
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Offline for <a href="">maintenance!</a>
        </h1>

        <p className={styles.description}>
          This app is undergoing maintenance right now.
          <br />
          Please check back later.
        </p>
        <div className={styles.grid}>
          <a href="https://twitter.com/CoderPY4" className={styles.card}>
            <h2>Check our twitter! &#10140;</h2>
            <p>
              Go to our twitter and check status or news. Also we in future add
              our blog!
            </p>
          </a>
          <a href="https://app.giveforms.com/forms/projectsofzero/default-giveform-2?type=popup" data-giveform="gf-widget" className={styles.card}>
            <h2>Support Me &#10140;</h2>
            <p>
              You can donate to our project. I will be very grateful for your support.
            </p>
          </a>
        </div>
      </main>

      <footer className={styles.footer}>
        <a href="https://instagram.com/coderpy.4" target="_blank" rel="noopener noreferrer">
          Made with ❤️ by CoderPY4
        </a>
      </footer>
    </div>
  );
}
