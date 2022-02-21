<?php 
include 'RestApi.php';
/**
 * Twitter
 *
 * with help of the API this class delivers all kind of tweeted images from twitter
 *
 * @package    socialstreams
 * @subpackage socialstreams/twitter
 * @author     ThemePunch <info@themepunch.com>
 */

class TP_twitter {

  /**
   * Consumer Key
   *
   * @since    1.0.0
   * @access   private
   * @var      string    $consumer_key    Consumer Key
   */
  private $consumer_key;

  /**
   * Consumer Secret
   *
   * @since    1.0.0
   * @access   private
   * @var      string    $consumer_secret    Consumer Secret
   */
  private $consumer_secret;

  /**
   * Access Token
   *
   * @since    1.0.0
   * @access   private
   * @var      string    $access_token    Access Token
   */
  private $access_token;

  /**
   * Access Token Secret
   *
   * @since    1.0.0
   * @access   private
   * @var      string    $access_token_secret    Access Token Secret
   */
  private $access_token_secret;

  /**
   * Initialize the class and set its properties.
   *
   * @since    1.0.0
   * @param      string    $api_key flickr API key.
   */
  public function __construct($consumer_key,$consumer_secret,$access_token,$access_token_secret) {
    $this->consumer_key         =   $consumer_key;
    $this->consumer_secret      =   $consumer_secret;
    $this->access_token         =   $access_token;
    $this->access_token_secret  =   $access_token_s